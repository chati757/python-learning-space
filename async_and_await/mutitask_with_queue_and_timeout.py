import asyncio
import random

# ผลลัพธ์ของแต่ละ task
results = {}

async def worker(id, limit):
    """ฟังก์ชันจำลองงานพร้อม timeout"""
    i = 0
    try:
        while i < limit:
            print(f"Task {id} is working... {i}")
            i += 1
            await asyncio.sleep(1)  # จำลองเวลาทำงาน
        results[id] = "Completed"  # บันทึกผลลัพธ์เมื่อเสร็จทันเวลา
    except Exception as e:
        results[id] = f"Failed: {str(e)}"  # บันทึกกรณีเกิดข้อผิดพลาดอื่น ๆ

async def task_manager():
    async def worker_consumer():
        """ดึงงานจาก queue มาทำงาน"""
        while True:
            id, limit, timeout = await queue.get()
            print(f"Starting Task {id}")
            try:
                # เพิ่ม timeout สำหรับแต่ละ task
                await asyncio.wait_for(worker(id, limit), timeout=timeout)
            except asyncio.TimeoutError:
                results[id] = "Timeout"
            print(f"Task {id} completed or timed out")
            queue.task_done()  # แจ้งว่า task เสร็จแล้ว

    # สร้าง consumer จำนวน 3 ตัว
    consumers = []
    # Queue สำหรับเก็บงาน
    queue = asyncio.Queue()

    # เพิ่ม task เริ่มต้น 3 ตัวลงใน queue
    await queue.put((1, 4, 2))  # กำหนด timeout ต่างกัน (กำหนดให้ทำงานไม่ทัน)
    await queue.put((2, 4, 5))  # กำหนด timeout ต่างกัน (กำหนดให้ทำงานทัน)
    await queue.put((3, 4, 5))  # กำหนด timeout ต่างกัน (กำหนดให้ทำงานทัน)

    # สร้าง worker มารับ task แต่ละ task (3 worker)
    consumers.append(asyncio.create_task(worker_consumer())) #(คาดว่าจะเกิด timeout)
    consumers.append(asyncio.create_task(worker_consumer())) #(คาดว่าไม่เกิด timeout)
    consumers.append(asyncio.create_task(worker_consumer())) #(คาดว่าไม่เกิด timeout)


    await asyncio.sleep(2)  # รอเพื่อจำลองการเพิ่ม task ใหม่
    # เพิ่ม task ใหม่เข้า queue
    await queue.put((4, 4, 5))  # เพิ่ม task ทีหลัง (กำหนดให้ทำงานไม่ทัน)
    # สร้าง worker มารับ task
    consumers.append(asyncio.create_task(worker_consumer()))

    # รอให้ queue ทำงานจนเสร็จ
    await queue.join()
    print('All tasks processed.')

    # ยกเลิก worker ทั้งหมดหลังงานเสร็จ
    for c in consumers:
        c.cancel()

    # แสดงผลลัพธ์ของแต่ละ task
    print("Task Results:")
    for task_id, status in results.items():
        print(f"Task {task_id}: {status}")

asyncio.run(task_manager())