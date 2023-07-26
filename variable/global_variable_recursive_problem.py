#test.py
print('test1')
from testlib import *
print('test3')


#testlib.py
print('test2')
from test import *
print('test4')

#output ถ้า run ด้วย test.py
'''
test1 เริ่มบรรทัดแรก และไป from testlib import * #[1]
test2 เข้าไปที่ testlib และ กลับไป from test import * #[2]
test1 เริ่มจากแรกใหม่เลย print test1
test3 skip from testlib import * เพราะ [1] เลยไปทำ test3 เลย
test4 เมื่อทำ test3 จบ กลับไปที่ [2] ของ testlib.py และทำ test4 ที่กำลังรออยู่
test3 หลังจาก test 4 กลับไปที่ [1] ของ test.py ที่กำลังรออยู่และ print test3
'''