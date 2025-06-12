#superclass
class a():
    def __init__(self):
        print('init a')
        print(f'call init self from b {self.fromb}')
        print(f'call init class from b {b}' )

    def somefunc(self):
        print('somefunc from a')
        print(f'call self from b {self.fromb}')
        print(f'call class from b {b}' )

#sub-class
class b(a):
    def __init__(self):
        self.fromb = 1
        # class b และ self ใน super ถูกส่งไปใช้ใน superclass (class a) และสามารถเรียกได้ ทั้ง b และ self 
        # สังเกตุที่ call self from b และ call class from b ด้านบน
        # ลำดับการ passing ต้อง class ก่อน object self เสมอ
        #print(super(,))#<super: <class 'b'>, <b object>>
        #print(super(b,self))#<super: <class 'b'>, <a object>>
        print(b)
        print(self)
        print(super(b,self))
        super(b,self).__init__()
        #super(b,self).__init__() #ส่วนนี้จะทำให้ __init__ ใน class a ทำงาน
        print('init b')


if __name__=='__main__':
    objb = b()
    print(objb)
    objb.somefunc() #การไม่ระบุ super(b,self).__init__() ไม่มีผลว่าจะสืบทอด function จาก class a ไม่ได้
    pass