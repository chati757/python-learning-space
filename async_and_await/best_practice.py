import asyncio
import signal

'''
อย่าลืมว่าการสั่ง await ต้องอยู่ภายใต้ async function เสมอ และ await คือการรอและขณะรอนั้นสามารถไปทำงานอื่นที่ await อื่นได้หาก await อื่นเสร็จก่อน
เหตุผลที่มันเป็น best_practice เพราะ 
1.task อื่นทำงานต่อไปได้ แม้มีบาง task ถูก cancel การทำงาน หรือ error เพราะ asyncio.gather มี return_exceptions=True และแต่ละ task ก็มี except ของตัวเอง
2.main_coru รองรับ asyncio.sleep()
3.main_coru รองรับ keyboard interrapt (signal)
4.กรณี coru มี infinite_loop การใช้ task.cancel() เช่น task1.cancel() สามารถหยุด infinite loop ได้สมบูรณ์ (แต่ต่างมี await ใน infinite loop ในที่นี้คือ await asyncio.sleep(1))
5.สามารถ break infinite loop ใน task ด้วย event
'''

async def coru_1(event):
    try:
        while True:
            print("coru 1 กำลังทำงาน...")
            await asyncio.sleep(1)

            print("event.wait กำลังรอ...")
            await event.wait()
            print('ถูก break ด้วย event.set')
            break

        print("coru 1 เสร็จสิ้น!")
    except asyncio.CancelledError:
        print('coru 1 ถูกยกเลิก')

async def coru_2():
    try:
        print("coru 2 กำลังทำงาน...")
        await asyncio.sleep(10)
        print("coru 2 เสร็จสิ้น!")
    except asyncio.CancelledError:
        print("coru 2 ถูกยกเลิก")

async def main_coru():
    event = asyncio.Event()

    task1 = asyncio.create_task(coru_1(event))
    task2 = asyncio.create_task(coru_2())

    await asyncio.sleep(2)
    task2.cancel()

    def stop_loop():
        print("ได้รับสัญญาณหยุด, กำลังหยุดโปรแกรม...")
        event.set()
        #task1.cancel()  # ทดลองยกเลิกเฉพาะ task1 task1 จะเข้า except asyncio.CancelledError event loop จะไม่หยุด

    # ดักจับสัญญาณ KeyboardInterrupt
    signal.signal(signal.SIGINT, lambda sig, frame: stop_loop())

    try:
        #await asyncio.gather(task1, task2)  # รันงานจนเสร็จ
        '''
        การใช้ return_exceptions เหมือนเป็นการมอบ except Exception : pass ให้ทุก task ใน gather 
        '''
        await asyncio.gather(task1, task2, return_exceptions=True)
    except Exception as e:
        print(e)
        print("งานถูกยกเลิก")
    finally:
        pass

# รัน event loop
'''
การสร้าง main_coru ทำให้เราสามารถ ใช้ await asyncio.sleep() และ await asyncio.gather ได้
'''

asyncio.run(main_coru())

print("loop close")