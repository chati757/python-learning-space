import asyncio

'''
หลักการสั่งให้ async function ทำงาน สามารถเลือกได้ว่าจะให้ รอจนเสร็จ หรือ
สั่งให้ทำงานแล้วระหว่างรอ async ของ task ทำงานเสร็จ สามารถไปทำอย่างอื่นก่อนได้ (ใน async ต้องมี await จึงสามารถออกไปทำอย่างอื่นระหว่างรอ await)
'''

async def async_1():
    print("Start async_1")
    await asyncio.sleep(1)
    print("Finish async_1")

async def async_2():
    print("Start async_2")
    await asyncio.sleep(1)
    print("Finish async_2")

async def async_3():
    print("Start async_3")
    await asyncio.sleep(2)
    print("Finish async_3")

async def main():
    # ต้องการให้ทำงานและระหว่างรอไปทำอย่างอื่นก่อนได้
    task_3 = asyncio.create_task(async_3())
    
    # ต้องการให้ทำงานและรอให้ async_1() ทำงานเสร็จก่อนจึงไปทำอย่างอื่น
    await async_1()
    
    # ต้องการให้ทำงานและรอให้ async_2() ทำงานเสร็จก่อนจึงไปทำอย่างอื่น
    await async_2()
    
    # รอให้ async_3 ทำงานเสร็จด้วยถ้า task3 หรือ async_3() เสร็จช้ากว่า async function อื่น คล้าย join thread
    await task_3

# เรียกฟังก์ชันหลัก
asyncio.run(main())

#เรายังสามารถ run แบบมีลำดับเหมือน sync ได้อีก 3 แบบดังต่อไปนี้
'''
#แบบที่ 1
def main():
    asyncio.run(async_1())  # เรียกใช้ async_1 แบบ sync และรอให้ทำงานเสร็จก่อน
    asyncio.run(async_2())  # เรียกใช้ async_2 แบบ sync และรอให้ทำงานเสร็จก่อน

main()
'''

'''
#แบบที่ 2
async def main():
    await asyncio.gather(
        async_1(),
        async_2(),
        # ...ฟังก์ชันอื่นๆ
    )

asyncio.run(main())
'''

'''
#แบบที่ 3
def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_1())
    loop.run_until_complete(async_2())

main()
'''