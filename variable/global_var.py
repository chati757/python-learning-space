test_global_var = 12

def call_global_var():
    '''
    การเรียกอ่าน global ทำได้ปกติหากไม่ได้ประกาศ test_global_var ไว้ใน function
    '''
    print('call in call global var')
    print(test_global_var) # 12

def edit_global_var():
    '''
    การแก้ไข variable global จะทำไม่ได้หากไม่ได้ ใส่ global test_global_var
    ไว้ใน function (หากไม่ใส่แต่ใช้ซื้อซ้ำจะเป็นการสร้างตัวแปรใหม่ใน lobal เท่านั้น)
    '''
    print('call in edit global var')
    #global test_global_var if not declare global it's will be local var.
    test_global_var = 14 # is local
    print(test_global_var)

if __name__ == "__main__":
    call_global_var()
    edit_global_var()
    print(test_global_var)
    pass