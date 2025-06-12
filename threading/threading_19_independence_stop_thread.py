import threading
import time

'''
# หากเราสามารถ thread มาหลาย thread แต่อยากปิดแค่บาง thread สามารถทำได้ตามตัวอย่างนี้
'''

class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._pause_event = threading.Event()  # สร้าง Event ภายใน class
        self._pause_event.set()  # เริ่มต้นให้ทำงานได้ทันที (Resume)

    def run(self):
        while True:
            self._pause_event.wait()  # หยุดรอถ้ายังไม่ได้ Resume
            print(f"{self.name} is running...")
            time.sleep(1)

    def pause(self):
        print(f"{self.name} paused.")
        self._pause_event.clear()  # หยุดทำงาน (Pause)

    def resume(self):
        print(f"{self.name} resumed.")
        self._pause_event.set()  # ทำงานต่อ (Resume)

    def stop(self):
        print(f"{self.name} stopped.")
        self._pause_event.set()  # ทำให้ thread หยุดการทำงาน (ทำให้ผ่าน wait() และออกจาก loop)
        raise SystemExit  # ใช้เพื่อหยุด thread นี้อย่างปลอดภัย

# สร้าง 3 thread
t1 = MyThread("Thread 1")
t2 = MyThread("Thread 2")
t3 = MyThread("Thread 3")

# เริ่มทำงานของทุก thread
t1.start()
t2.start()
t3.start()

# ทำงานสักพัก
time.sleep(3)
t1.pause()  # Pause Thread 1
time.sleep(2)
t2.pause()  # Pause Thread 2
time.sleep(2)
t3.pause()  # Pause Thread 3

# ทำงานต่อ
time.sleep(2)
t1.resume()  # Resume Thread 1
time.sleep(2)
t2.resume()  # Resume Thread 2
time.sleep(2)
t3.resume()  # Resume Thread 3

# หยุดทั้งหมด
time.sleep(3)
t1.stop()
t2.stop()
t3.stop()

# รอให้ threads หยุด
t1.join()
t2.join()
t3.join()

print("All threads are stopped.")
