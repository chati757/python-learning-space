import asyncio
import random

'''
เป็นการทดสอบการจ่ายงานจาก queue โดยในครั้งแรกสร้าง task เพื่อทำงาน 1-3 task
หลังจากนั้น แทรก task ที่ 4 ขณะที่ task 1-3 ยังคงทำงานอยู่ ซึ่งแม้ 1-3 task จะยังทำงานไม่จบ
ก็สามารถเริ่มงาน task 4 เพื่อทำควบคู่กับ 1-3 task ที่เริ่มก่อนหน้านั้นได้
'''

async def worker(id, limit):
    i = 0
    while i <= limit:
        print(f"Task {id} is working... {i}")
        i += 1
        await asyncio.sleep(random.uniform(0.5, 2))  # จำลองเวลาทำงาน

async def task_manager():
    # Queue สำหรับเก็บงาน
    queue = asyncio.Queue()

    # เพิ่ม task เริ่มต้น 3 ตัวลงใน queue
    for i in range(1, 4):
        await queue.put((i, random.randint(3, 5)))

    async def worker_consumer():
        """ดึงงานจาก queue มาทำงาน"""
        while True:
            id, limit = await queue.get()
            print(f"Starting Task {id}")
            await worker(id, limit)
            print(f"Task {id} completed")
            queue.task_done()  # แจ้งว่า task เสร็จแล้ว

    # สร้าง worker จำนวน 3 ตัว
    consumers = [asyncio.create_task(worker_consumer()) for _ in range(3)]

    # เพิ่ม task ใหม่เข้า queue
    await queue.put((4, 4))

    # เพิ่ม worker ใหม่เฉพาะ task 4 เพื่อทำงานทันที หลังจากรอ task 1-3 ทำงานไปแล้ว 2 วินาที
    await asyncio.sleep(2)
    consumers.append(asyncio.create_task(worker_consumer()))

    # รอให้ queue ทำงานจนเสร็จ
    await queue.join()
    print('end all task')

    # ยกเลิก worker ทั้งหมดหลังงานเสร็จ
    for c in consumers:
        c.cancel()

asyncio.run(task_manager())