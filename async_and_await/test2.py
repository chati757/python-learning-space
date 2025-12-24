import asyncio

async def task1():
    print("task1: ก่อนนอน")
    await asyncio.sleep(1)  # รอ 1 วิ (คืน control ให้ event loop)
    print("task1: หลังตื่น")  # ← จะไม่ถูกพิมพ์ออกมา หาก task2 block อยู่

async def task2():
    print("task2: เริ่ม loop")
    for i in range(100000):  # ใหญ่มาก ไม่มี await เลย
        print('do in task2')
        pass
    print("task2: จบ loop")

async def main():
    await asyncio.gather(task1, task2)

asyncio.run(main())