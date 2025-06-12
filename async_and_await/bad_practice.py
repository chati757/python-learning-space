import asyncio

async def task_1():
    print("Task 1 กำลังทำงาน...")
    await asyncio.sleep(7)
    print("Task 1 เสร็จสิ้น!")

async def task_2():
    print("Task 2 กำลังทำงาน...")
    await asyncio.sleep(10)
    print("Task 2 เสร็จสิ้น!")

async def main():
    task1 = asyncio.create_task(task_1())
    task2 = asyncio.create_task(task_2())

    await asyncio.sleep(2)  # รอให้ task1 ทำงานก่อน
    task1.cancel()  # ยกเลิก task1
    #task2.cancel()

    try:
        await asyncio.gather(task1, task2)  # รันงานจนเสร็จ
        #await asyncio.gather(task1, task2, return_exceptions=True)
    
        '''
        ไม่ควรใช้ asyncio.CancelledError กับ await asyncio.gather เพราะเมื่อ task1.cancel() ทำงาน
        มันจะ bypass await asyncio.gather(task1, task2) ไป loop close (แม้ task2 ทำงานอยู่)
        ในส่วนนี้การทำให้ task2 ปิดแบบถูกบังคับ (ปิดไม่สมบูรณ์)(ไม่มีโอกาสได้จัดการก่อนปิด)
        '''
    except asyncio.CancelledError:
        print("งานถูกยกเลิก")
    finally:
        pass

# รัน event loop
asyncio.run(main())
print("loop close")