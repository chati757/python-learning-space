import threading
import time
import os
import psutil

'''
ถ้า sub-thread error โดยไม่มีการ try-except สำหรับ thread join() ที่สร้างใน main-thread จะทำงานอย่างไร
คำตอบคือ เมื่อ error ใน sub-thread join() จะรับทราบว่า sub-thread ทำงานจบ เหมือน sub-thread ทำงานจบทั่วๆไป
'''

def thread_function():
    # ยกข้อผิดพลาด
    print(f'sub-thread id : {threading.get_ident()}')
    print('waiting in thread')
    time.sleep(4)
    raise ValueError("An error occurred in the thread!")

def list_python_pids():
    python_pids = []
    
    # ตรวจสอบทุก process
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # ตรวจสอบชื่อ process ว่าเป็น 'python' หรือไม่
            if 'python' in proc.info['name']:
                print(f"{proc.info['name']} : {proc.info['pid']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return python_pids


print(os.getpid())
# สร้างและเริ่มต้น thread
thread = threading.Thread(target=thread_function)
thread.start()

# รอให้ thread เสร็จสิ้น
print('before join')
thread.join()
print('after join')

print("Thread has finished executing.")

# แสดง PID ของ Python processes
list_python_pids()