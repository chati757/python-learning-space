import asyncio

class MyAsyncContextManager:
    async def __aenter__(self):
        # ประกาศการเข้าสู่ asynchronous context
        print("Entering the async context")
        return self

    async def somefunc(self):
        print('somefunc : waiting')
        await asyncio.sleep(3)
        print('somefunc : finish')
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        # ประกาศการออกจาก asynchronous context
        print("Exiting the async context")

async def main():
    async with MyAsyncContextManager() as macm:
        await macm.somefunc()
        print("Inside the async context")

if __name__ == '__main__':
    asyncio.run(main())