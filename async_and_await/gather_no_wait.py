import asyncio

'''
asyncio.gather ถูกสั่งให้รอ 2 task แต่พบว่า task2 เกิด error
ทำให้ gather ไม่รอ task1 ทำงานเสร็จ ,เพราะ task2 เกิด raise asyncio.gather จึงสั่ง cancel task ทุก task ที่มี เมื่อ return_exception=False

แต่หากสั่ง return_exception = True 
task1 ก็ยังคงทำงานต่อไปได้แม้ task2 จะ error ไปแล้วก็ตาม
และจะให้ผลลัพธ์ใน result เป็น ['Task 1 result', ValueError('Error in Task 2')] แทน
'''

async def task1():
    try:
        print("Task 1 started")
        await asyncio.sleep(5)
        print("Task 1 completed")
    except asyncio.CancelledError:
        print('task 1 cancel')
    return "Task 1 result"

async def task2():
    print("Task 2 started")
    await asyncio.sleep(4)
    raise ValueError("Error in Task 2")  # Task 2 เกิด exception

async def main():
    try:
        result = await asyncio.gather(task1(), task2(), return_exceptions=False)
        print(result)

    except asyncio.CancelledError:
        print(f"Exception caught in gather")


try:
    asyncio.run(main())

except Exception as e:
    print(e)