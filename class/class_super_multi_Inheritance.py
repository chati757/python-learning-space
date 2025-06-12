class A():
    def __init__(self):
        print('init A')
    def method_a(self):
        print("Method A")

class B():
    def __init__(self):
        print('init B')

    def method_b(self):
        print("Method B")

class C(A, B):
    def __init__(self):
        print('-----init c------')
        super().__init__()
        super().method_a()
        super().method_b()
        #super(A,self).method_a() #รุะบุแบบนี้ใช้งานไม่ได้
        #super(B,self).method_b() #รุะบุแบบนี้ก็ใช้งานไม่ได้
        super(C,self).method_a() #ระบุแบบนี้ได้อย่างเดียวเท่านั้น super(C,self) และจะเรีนก method_a หรือ metthod_b ก็ได้
        super(C,self).method_b() #ระบุแบบนี้ได้อย่างเดียวเท่านั้น super(C,self) และจะเรีนก method_a หรือ metthod_b ก็ได้
        print('--end of init c--')
    
    def method_c(self):
        print('Method C')

c_instance = C() # class c เลือกที่จะ init B เพราะ C ไม่มี __init__ ของตัวเอง
# กรณี class A ไม่มี __init__ ของมันเอง class c ก็จะไปเรียก __init__ ของ class B ในลำดับถัดไป
c_instance.method_a()  # ผลลัพธ์: Method A
c_instance.method_b()  # ผลลัพธ์: Method B
c_instance.method_c()