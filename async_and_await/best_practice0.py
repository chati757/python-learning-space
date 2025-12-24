import asyncio
from rich import print
import sys
import inspect

async def task_1():
    try:
        print("Task 1 กำลังทำงาน...")
        #raise Exception('test')
        await asyncio.sleep(7)
        print("Task 1 เสร็จสิ้น!")
    except asyncio.CancelledError:
        print('Task 1 : cancel')
        raise
    except Exception as e:
        print(f'{inspect.currentframe().f_code.co_name} : error : {str(sys.exc_info()[2].tb_lineno)} : {e}')
        raise

async def task_2():
    try:
        print("Task 2 กำลังทำงาน...")
        await asyncio.sleep(10)
        print("Task 2 เสร็จสิ้น!")
    except asyncio.CancelledError:
        print('Task 2 : cancel')
        raise

async def main():
    result = None
    task1 = asyncio.create_task(task_1())
    task2 = asyncio.create_task(task_2())
    try:
        #await asyncio.sleep(2)  # รอให้ task1 ทำงานก่อนแต่ยังไม่เสร็จ
        #task1.cancel()  # ยกเลิก task1 ทั้งๆที่ยังไม่เสร็จ
        #task2.cancel()

        print('before gather')
        result = await asyncio.gather(task1, task2)  # รันงานจนเสร็จ
        #result = await asyncio.gather(task1, task2, return_exceptions=True) #เก็บ exception error ไว้ใน result ไม่ raise ออกมาและทำให้ task อื่นๆที่ทำงานได้ปกติพังไปด้วย
        print('after gather')
    
        '''
        ไม่ควรใช้ asyncio.CancelledError กับ await asyncio.gather เพราะเมื่อ task1.cancel() ทำงาน
        มันจะ bypass await asyncio.gather(task1, task2) ไป loop close (แม้ task2 ทำงานอยู่)
        ในส่วนนี้การทำให้ task2 ปิดแบบถูกบังคับ (ปิดไม่สมบูรณ์)(ไม่มีโอกาสได้จัดการก่อนปิด)
        '''
    except asyncio.CancelledError:
        print("งานถูกยกเลิก")
    except Exception as e:
        print(f'{inspect.currentframe().f_code.co_name} : error : {str(sys.exc_info()[2].tb_lineno)} : {e}')
    finally:
        if result:
            print(result)
        else:
            print('no result')

        print(asyncio.all_tasks()) #เหลือแค่ task main
        pass

# รัน event loop
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('keyboard interrupt')

print("loop close")