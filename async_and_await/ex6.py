import asyncio

async def job():
    await asyncio.sleep(2)
    return "OK"

async def main():
    task = asyncio.create_task(job())

    if await task:
        print("✅ Task ได้ผลลัพธ์ที่ truthy (เช่น OK)")
    else:
        print("❌ Task ได้ผลลัพธ์ที่ falsy (เช่น None, False, 0)")

asyncio.run(main())
