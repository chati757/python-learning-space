class A:
    def __init__(self):
        print('init from A')
    def func_from_a(self):
        print('func_from_a is running')

class B(A):
    def __init__(self):
        super(B).__init__() #run ผ่านแต่เงียบ (ทำไม?) เหมือนถูกสั่ง pass
        '''
        เปรียบเหมือนการระบุครึ่งๆกลางมันจึงไม่ทำงานและผ่านไป
        ในส่วนของ super(B).__init__() การใช้ super() 
        โดยไม่ระบุ self จะไม่ทำงานอย่างถูกต้อง เพราะไม่ได้ระบุ instance(self)
        ปัจจุบันของคลาส B ซึ่งทำให้ไม่สามารถเรียก constructor (__init__) 
        ของ superclass(class A) ได้
        '''

        super(B,self).__init__() #ทำงานได้ปกติ
        '''
        เมื่อใช้ super(B,self).__init__() คือการระบุ instance ปัจจุบันของคลาส B โดยชัดเจน (มันจึงทำงาน)
        เพื่อให้ Python สามารถรู้ว่าในการเรียก constructor ของ superclass 
        ควรใช้ instance ของคลาส B จึงทำให้การเรียก __init__() ของ superclass ใช้งานได้อย่างถูกต้อง
        '''

        super(B).func_from_a()#error , AttributeError: 'super' object has no attribute 'func_from_a'
        '''
        เปรียบเหมือนการระบุครึ่งๆกลางมันจึงไม่ทำงานและผ่านไป เหมือนกรณี super(B).__init__()
        '''
        super(B,self).func_from_a()#ทำงานได้ปกติ
        '''
        เมื่อใช้ super(B,self).func_from_a() คือการระบุ instance ปัจจุบันของคลาส B โดยชัดเจน (มันจึงทำงาน)
        เหมือน super(B,self).__init__()
        '''

b_instance = B()