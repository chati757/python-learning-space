import asyncio

class AsyncIterator:
    def __init__(self, max_number):
        self.current = 0
        self.max_number = max_number

    def __aiter__(self):
        #จะถูกเรียกในครั้งแรกเมื่อ async for เพื่อตรวจสอบว่า class มีคุณสมบัติจะเป็น asynchronous iterator ได้หรือไม่
        #ถ้าไม่เกิด error จะเรียก __anext__ เพื่อทำงานใรครั้งถัดไปตาม การกำหนดของ __anext__
        return self  # คืนตัวเองเป็น iterator

    async def __anext__(self):
        if self.current < self.max_number:
            await asyncio.sleep(1)  # จำลองการรอข้อมูล
            self.current += 1
            return self.current
        else:
            raise StopAsyncIteration

async def main():
    async for number in AsyncIterator(5):
        print(number)

asyncio.run(main())