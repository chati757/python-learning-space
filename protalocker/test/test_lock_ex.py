import portalocker
import time

# กำหนด path ของไฟล์ที่ต้องการล็อก
file_path = './data.pkl'

try:
    # เปิดไฟล์ในโหมด 'r+' (อ่าน/เขียน) หรือ 'w' (สร้างไฟล์ถ้าไม่มี)
    with open(file_path, 'r+') as file:  # ใช้ 'w' เพื่อสร้างไฟล์เปล่าหากยังไม่มี
        print(f"Locking the file '{file_path}'...")
        # ล็อกไฟล์แบบ Exclusive
        portalocker.lock(file, portalocker.LOCK_EX)
        
        # ไฟล์ถูกล็อก รอ 15 วินาที
        print('locking in 15 second..')
        time.sleep(15)

        # ปลดล็อกไฟล์ (ปิดไฟล์อัตโนมัติเมื่อออกจาก with)
        portalocker.unlock(file)
        print(f"Unlocking the file '{file_path}'...")

except portalocker.exceptions.LockException:
    print("Failed to lock the file. It may be locked by another process.")