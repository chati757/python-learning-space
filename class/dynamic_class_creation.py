'''
# โดยปกติการสร้าง class เราจะเป็นต้องระบุชื่อ class , inherit ผ่าน super และสร้าง attribute ผ่าน __init__(self)
# แต่ด้วยการสร้าง class แบบ Dynamic เราสามารถสร้าง class โดยใช้ type ในการสร้าง 
'''

class BaseClass:
    def greet(self):
        print("Hello from BaseClass")

# สร้างคลาสใหม่ที่สืบทอดจาก BaseClass
DerivedClass = type('DerivedClass', (BaseClass,), {'x': 20})

# ใช้งานคลาสที่สร้างขึ้น
obj = DerivedClass()
obj.greet()      # เรียกใช้เมธอดจาก BaseClass
print(obj.x)     # แสดงค่า 20