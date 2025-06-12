import asyncio
from collections import defaultdict
import functools
import time
from rich import print

class AsyncMultiRateLimiter:
    def __init__(self):
        self.queues = defaultdict(asyncio.Queue)
        self.min_intervals = {}
        self.last_called = defaultdict(lambda: 0)
        self.workers = {}
        self._shutdown_event = asyncio.Event()

    def cooldown(self, interval_seconds):
        """
        Decorator ที่ใช้แทนการเรียก .set_cooldown()
        """
        def decorator(func):
            func_name = func.__name__
            self.min_intervals[func_name] = interval_seconds

            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                if func_name not in self.workers:
                    self.workers[func_name] = asyncio.create_task(self.worker(func_name))
                await self.queues[func_name].put((func, args, kwargs))

            return wrapper
        return decorator

    async def worker(self, func_name):
        queue = self.queues[func_name]
        while not self._shutdown_event.is_set():
            try:
                func, args, kwargs = await asyncio.wait_for(queue.get(), timeout=1)
            except asyncio.TimeoutError:
                continue

            now = asyncio.get_event_loop().time()
            elapsed = now - self.last_called[func_name]
            cooldown = self.min_intervals[func_name]

            if elapsed < cooldown:
                sleep_time = cooldown - elapsed
                print(f"\\[{func_name}] Cooldown {sleep_time:.2f}s")
                await asyncio.sleep(sleep_time)

            try:
                await func(*args, **kwargs)
            except Exception as e:
                print(f"\\[{func_name}]  [red]ERROR:[/red] {e}")
            finally:
                self.last_called[func_name] = asyncio.get_event_loop().time()
                queue.task_done()

    async def shutdown(self):
        await asyncio.gather(*[q.join() for q in self.queues.values()])
        print("Shutting down rate limiter...")
        self._shutdown_event.set()
        for func_name, task in self.workers.items():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                print(f"Worker '{func_name}' cancelled.")

# ====== ใช้งาน =======

limiter = AsyncMultiRateLimiter()
@limiter.cooldown(1)
async def send_order(order_type, price):
    print(f"\\[send_order] [yellow]{order_type} at {price}[/yellow]")
    if order_type == "error":
        raise ValueError("[red]Simulated send_order : error[/red]")

@limiter.cooldown(1)
async def send_future_order(order_type,price):
    print(f'\\[send_future_order] [yellow]{order_type} at {price}[/yellow]')
    if order_type == "error":
        raise ValueError("[red]Simulated send_future_order : error[/red]")

async def main():
    try:
        print('Sending orders...')
        await send_order("limit", 1000)
        await send_order("market", 1001)
        await send_future_order('limit',9999)
        await send_future_order('market',4444)
        await send_order("error",1234)
        await send_future_order('error',1001)
        await send_order("limit", 1002)
        print('All orders sent')
    finally:
        await limiter.shutdown()


# รัน main
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program interrupted.")
