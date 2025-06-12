import threading
import time

def print_message():
    print("Timer expired!")

# สร้าง Timer object
timer = threading.Timer(1, print_message)

# ตั้งค่าเป็น daemon
timer.daemon = True

# เริ่มต้น Timer
timer.start()

print("Timer started")

time.sleep(10)

# ไม่รอให้ Timer ทำงานเสร็จ และ thread จะไม่ค้างเป็น zombie เพราะเรา set daemon เป็น True แต่ถ้าเรา uncomment timer.join() จะรอให้ timer thread ทำงานเสร็จก่อน
# timer.join()