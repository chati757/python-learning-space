class MyClass():
    def __new__(cls, *args, **kwargs):
        print("Creating instance")
        print(cls) #<class '__main__.MyClass'> คือแม่แบบ
        instance = super().__new__(cls)  # คือ object ที่สร้างโดยอ้างอิงแม่แบบ <__main__.MyClass object at 0x000001D9D839EEB0>
        print(instance) #<__main__.MyClass object at 0x000001D9D839EEB0>
        return instance

    def __init__(self, value):
        print("Initializing instance")
        print(self)
        self.value = value

    def __del__(self):
        print("Destroying instance")

# สร้างอ็อบเจกต์
obj = MyClass(10)
print(obj)#<__main__.MyClass object at 0x000001D9D839EEB0>
# ลบอ็อบเจกต์
del obj