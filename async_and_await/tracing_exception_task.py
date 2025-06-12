import asyncio
import time
import sys
import inspect

'''
CustomCancelledErrorMessage เอาไว้ส่งข้อความหา async main เพราะการจับ except asyncio.CancelledError
ใน task ไม่สามารถส่งข้อความไปยัง async main ได้ทำให้การติดตาม error เป็นไปได้ยาก CustomCancelledErrorMessage
จึงเข้ามาแก้ไข ทำให้ส่งข้อความได้และระบุจุดที่ error ได้อย่างถูกต้อง
'''

class CustomCancelledErrorMessage(BaseException):  # BaseException ใช้สำหรับ asyncio
    def __init__(self, message="Task was cancelled"):
        super().__init__(message)  # กำหนดข้อความไปที่ args[0]
        self.message = message

    def __str__(self):
        return self.message  # ทำให้ str(e) แสดงข้อความถูกต้อง

async def task1():
    try:
        print("Task1: Started")
        await asyncio.sleep(3)
        raise ValueError('test')
        print("Task1: Completed")
    except asyncio.CancelledError:
        raise CustomCancelledErrorMessage(f'{inspect.currentframe().f_code.co_name} : error {str(sys.exc_info()[2].tb_lineno)} : some error at')

async def main():
    t1 = asyncio.create_task(task1())
    await asyncio.sleep(1)  # รอให้ task เริ่มทำงาน
    t1.cancel()  # ยกเลิก task1
    
    try:
        await t1  # รอให้ task ถูกยกเลิกจริง ๆ
    except CustomCancelledErrorMessage as e:
        print(e)
        print(str(sys.exc_info()[2].tb_lineno))

try:
    asyncio.run(main())
    time.sleep(5)
except KeyboardInterrupt:
    print("Main function: KeyboardInterrupt detected")
