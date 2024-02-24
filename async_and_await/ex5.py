import asyncio

async def my_async_function():
    print("Start")

    # ทำงานอื่น ๆ ที่ไม่ต้องรอ
    asyncio.create_task(do_something_else('first'))
    #ก่อน await (บรรทัด 9) มี task ที่ไม่ได้ run คือ asyncio.create_task(do_something_else('first')) มันจึง run asyncio.create_task(do_something_else('first')) ก่อน
    await asyncio.create_task(do_something_else('second'))
    print('Waiting 10 seconds')
    await asyncio.sleep(10) #ถ้า task ที่ create ไม่ได้สั่ง run มันจะ run เองก่อนเจอ await
    print("After 10 seconds")

async def do_something_else(data):
    print(f"Doing something else : {data}")

# ตัวอย่างการใช้งาน
asyncio.run(my_async_function())