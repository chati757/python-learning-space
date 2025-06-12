'''
หากเราต้องการให้ class ถูกนำไปเรียกใช้ได้หลาย script แต่ไม่ต้องการให้เรียกใช้พร้อมกัน
เช่น เมื่อ script1 แรกเรียกใช้ function ใน class หากมี script2 ต้องการเข้ามาใช้งาน
ในขณะนั้นมันจะต้องรอจนกว่า script1 ใช้งาน function เสร็จก่อนและ script2 จึงจะเริ่ม
เข้ามาใช้งานเป็นต้น
'''

import portalocker
import time

# ฟังก์ชันที่ต้องการล็อก
def critical_function(task):
    # สร้างไฟล์ล็อก
    with portalocker.Lock("shared.lock", timeout=10) as lock_file:
        print(f"{task} is running")
        time.sleep(5)  # จำลองการทำงาน
        print(f"{task} is done")