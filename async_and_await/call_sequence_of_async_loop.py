import asyncio

async def work_a():
    print("A1")
    await asyncio.sleep(1)
    print("A2")
    await asyncio.sleep(3)
    print("A3")

async def work_b():
    print("B1")
    await asyncio.sleep(2)
    print("B2")
    await asyncio.sleep(4)
    print("B3")

async def async_function_no_sleep():
    print('async_function_no_sleep')

async def async_function_with_sleep():
    await asyncio.sleep(0)
    print('async_function_with_sleep')

async def main():
    loop = asyncio.get_running_loop()

    loop.call_soon(lambda: print("SOON")) #เร็วเท่า create task

    task_a = asyncio.create_task(work_a())
    task_b = asyncio.create_task(work_b())

    await async_function_with_sleep() #ช้ากว่า create task , task-ready state

    loop.call_later(0, lambda: print("LATER")) #ช้ากว่า task-ready state แม้จะ sleep 0 เท่ากันเพราะอยู่ใน timer heap state ต้องรอย้ายมาลง read task state เมื่อพร้อมเหมือน task ready state

    await async_function_no_sleep()
    await asyncio.gather(task_a, task_b)

if __name__=='__main__':
    asyncio.run(main())

'''
โครงสร้างลำดับใน async loop

Iteration N
  1) run ready callbacks
  2) run ready tasks (await resume) (ready task state)
  3) I/O poll
  4) check timers (timer heap state)
  5) (promote expired timers state) expired timers → ready callbacks (move to ready task state)

Iteration N+1
  1) run ready task callback from expired timers
'''