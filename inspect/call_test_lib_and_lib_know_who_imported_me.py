from test_lib import *

'''
เป็นการทำสอบเรียก lib แล้ว lib รู้ว่า file ไหนกำลัง import มัน
โดย lib จะแสดง file call_test_lib_and_lib_know_who_imported_me.py 
ว่ากำลัง import มัน
'''

if __name__=='__main__':
    print('in main')
    who_imported_me()