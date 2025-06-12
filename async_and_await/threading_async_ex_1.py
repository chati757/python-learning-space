import asyncio
import threading
from typing import List

async def fetch_data(item: str) -> str:
    await asyncio.sleep(1)  # simulate async task
    return f"Processed {item}"

async def process_all_tasks(task_names: List[str]) -> List[str]:
    tasks = [fetch_data(name) for name in task_names]
    results = await asyncio.gather(*tasks)
    return results

def run_in_sub_thread(task_names: List[str]):
    # สร้าง event loop ใหม่สำหรับ sub-thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    # รัน async tasks บน event loop ของ sub-thread
    results = loop.run_until_complete(process_all_tasks(task_names))
    
    print("Results from sub-thread:", results)
    loop.close()

# รายการ tasks ที่จะส่งเข้าไป
task_list = ["Task1", "Task2", "Task3"]

# สร้าง sub-thread เพื่อรัน asyncio task
sub_thread = threading.Thread(target=run_in_sub_thread, args=(task_list,))
sub_thread.start()
sub_thread.join()  # รอให้ sub-thread ทำงานเสร็จ