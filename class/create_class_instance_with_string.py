'''
# การเราต้องการสร้าง instance ของ class โดยเรียก class template ด้วย string

class template คืออะไร มันคือ class แม่แบบเช่น 
class A():
    def __init__(self,name):
        self.name = name

หรือ 

type('B',(),{
    '__init__':(lambda self,name:setattr(self, 'name', name))

})

class instance คืออะไร 

test_a = a() # test_a คือ instance เป็นต้น
test_b = b() # test_b คือ instance เป็นต้น
'''

#สร้าง class template

class a_template():
    def __init__(self,name):
        self.name = name

class b_template():
    def __init__(self,name):
        self.name = name

#การสร้าง class template dict เพื่อใช้เรียกด้วย string โดย filter defualt instance ออก
template_class_dict = { k:v for k,v in globals().items() if(not k.startswith('__'))}

print(template_class_dict) #{'a_template': <class '__main__.a_template'>, 'b_template': <class '__main__.b_template'>}

a_instance = template_class_dict['a_template']('test_name')

print(a_instance.name)