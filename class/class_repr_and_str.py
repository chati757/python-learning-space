class Example:
    def __init__(self, x):
        self.x = x
    
    def __repr__(self):
        return f"Example({self.x})"
    
    def __str__(self):
        return str(self.x)
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.x + other
        elif isinstance(other, Example):
            return self.x + other.x
        return NotImplemented  # คืนค่า NotImplemented ถ้า other ไม่ใช่ int, float หรือ Example
    
    def __radd__(self, other):
        return self.__add__(other)  # สำหรับการสนับสนุนการบวกจากมุมมองของ other

# การใช้งาน
a = Example(2)
b = Example(3)

print(a + b)   # Output: 5 (ใช้ a.__add__(b))
print(a + 5)   # Output: 7 (ใช้ a.__add__(5))
print(5 + a)   # Output: 7 (ใช้ a.__radd__(5))

c = "hello"
print(a + c)   # Raises TypeError: unsupported operand type(s) for +: 'Example' and 'str'

'''
“`NotImplemented` ถูกใช้ในเมธอดทางคณิตศาสตร์เพื่อบอก 
Python ว่าการดำเนินการที่ร้องขอไม่ได้รับการสนับสนุนสำหรับประเภทของอาร์กิวเมนต์ที่ให้มา. 
เมื่อ `NotImplemented` ถูกคืนค่า, Python จะลองเรียกเมธอดผกผัน 
(เช่น `__radd__` สำหรับการบวก) และถ้าเมธอดผกผันคืนค่า 
`NotImplemented` เช่นกัน, Python จะยกข้อผิดพลาด

กรณี NotImplemented ทำงาน

คือ print(5 + a)   # Output: 7 (ใช้ a.__radd__(5))

เรียก 5.__add__(a) แต่เนื่องจาก int ไม่มีเมธอด __add__ ที่รองรับ Example, คืนค่า NotImplemented
Python ลองเรียก a.__radd__(5)
a.__radd__(5) เรียก a.__add__(5) ภายใน, ดังนั้นคืนค่า self.x + other (2 + 5) = 7

และ c = "hello" ; print(a + c) 
พยายามใช้ "hello".__radd__(a) แล้ว แต่ไม่ได้ผล จึง raise TypeError ออกมา
'''