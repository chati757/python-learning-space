import asyncio
from typing import Set

# ✅ เก็บ task ที่สร้างขึ้นทั้งหมด
active_tasks: Set[asyncio.Task] = set()

def track_task(coro) -> asyncio.Task:
    """
    สร้าง task ใหม่ และ track มันใน active_tasks
    """
    task = asyncio.create_task(coro)
    active_tasks.add(task)

    def on_done(t: asyncio.Task):
        # ดึง exception เพื่อไม่ให้ warning "exception was never retrieved"
        try:
            result = t.exception()
            if(result):
                print(result)
        except Exception:
            pass
        # ❌ ลบ task ออกจาก set
        active_tasks.discard(t)

    task.add_done_callback(on_done)
    return task

#---------------แนวทางการใช้งาน-------------------
async def do_work(name, delay):
    await asyncio.sleep(delay)
    if delay % 2 == 0:
        raise ValueError(f"Task {name} พังงงงง")
    print(f"✅ Task {name} เสร็จแล้ว")

async def main():
    track_task(do_work("A", 2))
    track_task(do_work("B", 3))
    track_task(do_work("C", 1))

    while active_tasks:
        print(f"📋 ยังมี task อยู่: {len(active_tasks)}")
        await asyncio.sleep(0.5)

asyncio.run(main())