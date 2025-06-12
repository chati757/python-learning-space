import asyncio

class AsyncNumberGenerator:
    def __init__(self, max_number):
        self.max_number = max_number

    def __aiter__(self):
        # คืน iterator ของ class อื่น
        return AsyncIterator(self.max_number)

class AsyncIterator:
    def __init__(self, max_number):
        self.current = 0
        self.max_number = max_number

    def __aiter__(self):
        return self  # คืนตัวเองเป็น iterator

    async def __anext__(self):
        if self.current < self.max_number:
            await asyncio.sleep(1)  # จำลองการรอข้อมูล
            self.current += 1
            return self.current
        else:
            raise StopAsyncIteration

async def main():
    async for number in AsyncNumberGenerator(5):
        print(number)

asyncio.run(main())