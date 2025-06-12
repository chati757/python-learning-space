import asyncio
from collections import defaultdict

#asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class AsyncMultiRateLimiter:
    def __init__(self):
        self.queues = defaultdict(asyncio.Queue)
        self.min_intervals = {}  # map: func_name -> interval_seconds
        self.last_called = defaultdict(lambda: 0)
        self.workers = {}
        self._shutdown_event = asyncio.Event()

    def set_cooldown(self, func_name, interval_seconds):
        self.min_intervals[func_name] = interval_seconds
        if func_name not in self.workers:
            self.workers[func_name] = asyncio.create_task(self.worker(func_name))

    async def worker(self, func_name):
        queue = self.queues[func_name]
        while not self._shutdown_event.is_set():
            try:
                print('loop worker : running')
                func, args, kwargs = await asyncio.wait_for(queue.get(), timeout=1)
                print('queue release')

            except asyncio.TimeoutError:
                continue  # allow checking shutdown every 0.5s

            now = asyncio.get_event_loop().time()
            elapsed = now - self.last_called[func_name]
            cooldown = self.min_intervals[func_name]

            if elapsed < cooldown:
                sleep_time = cooldown - elapsed
                print(f"[{func_name}] Cooldown {sleep_time:.4f}s")
                await asyncio.sleep(sleep_time)

            try:
                await func(*args, **kwargs)
            except Exception as e:
                print(f"[{func_name}] ERROR: {e}")
            finally:
                self.last_called[func_name] = asyncio.get_event_loop().time()
                print('queue.task_done')
                queue.task_done()

    async def call(self, func, *args, **kwargs):
        func_name = func.__name__
        if func_name not in self.min_intervals:
            raise ValueError(f"No cooldown set for function '{func_name}'")
        await self.queues[func_name].put((func, args, kwargs))

    async def shutdown(self):
        # รอให้ queue ทุกตัวของ worker ทำงานเสร็จก่อน
        await asyncio.gather(*[q.join() for q in self.queues.values()])

        print("Shutting down rate limiter...")
        self._shutdown_event.set()

        # ยกเลิก worker ทั้งหมด
        for func_name, task in self.workers.items():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                print(f"Worker '{func_name}' cancelled.")

async def send_order(order_type, price):
    print(f"[SEND ORDER] {order_type} at {price}")
    if order_type == "error":
        raise ValueError("Simulated order error")

async def main():
    limiter = AsyncMultiRateLimiter()
    limiter.set_cooldown("send_order", 0.5) #สร้าง task worker
    #await asyncio.sleep(0) #return control ไปกลับให้ event loop เพื่อให้ woeker ทำงาน
    try:
        print('limit1')
        '''
        #การทำงาน await limiter.call(send_order, "limit",1000) function จะยังคงทำให้ control ยังคงกลับมา caller task 
        #(แม้เป็น await แต่เป็น await ที่ไม่ทำให้เกิดการรอใน function (limiter.call) 
        #เลยมันจึงไม่สามารถสลับไปทำ task อื่นที่รอได้ส่วนนี้เลยเป็นเหมือน sync function ธรรมดาเลยและก็ทำบรรทัดต่อไปซึ่งมีพฤติกรรมคล้ายกัน)
        '''
        await limiter.call(send_order, "limit",1000) 
        print('limit2')
        await limiter.call(send_order, "market",1001)
        #await asyncio.sleep(10)
        print('end of call')

    except asyncio.CancelledError:
        print("Main task was cancelled.")
    
    finally:
        # Ensure that shutdown happens even if task is cancelled or error occurs
        await limiter.shutdown()

# Run the program with error handling for KeyboardInterrupt
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Program interrupted. Shutting down gracefully...")
