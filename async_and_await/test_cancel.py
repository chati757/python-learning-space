import asyncio

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def task3():
    try:
        print('start task3')
        await asyncio.sleep(5)
        print('end task3')
    except asyncio.CancelledError:
        print('task3 cancelled')
        raise

async def task2():
    try:
        print('start task2')
        t3 = asyncio.create_task(task3())
        await t3
        print('end task2')
    except asyncio.CancelledError:
        print('task2 cancelled')
        raise

async def task1():
    try:
        print('start task1')
        t2 = asyncio.create_task(task2())
        await t2
        print('end task1')
    except asyncio.CancelledError:
        print('task1 cancelled')
        raise

async def main():
    try:
        print('start main')
        t1 = asyncio.create_task(task1())
        await t1
        print('end main')
    except asyncio.CancelledError:
        print('main cancelled')

try:
    asyncio.run(main())

except KeyboardInterrupt:
    print('inkeyboard interup')