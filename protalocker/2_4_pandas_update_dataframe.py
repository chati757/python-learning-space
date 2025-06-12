# -*- coding: utf-8 -*-

import pandas as pd
import portalocker

'''
flags=portalocker.LOCK_EX | portalocker.LOCK_NB
มีความหมายว่า ให้ใช้ share_lock (สำหรับ write [lock ได้ทีละ process ไม่สามารถ lock หลาย process พร้อมกัน]) แต่หากเจอว่า share lock หรือ exclusive lock จะต้องรอ แต่เป็นการรอแบบ lock_nb คือรอแบบ non-block โดยมี timeoutเมื่อรอเป็นระยะเวลานึงจะ non-block และ raise
'''

def safe_update_dataframe_to_csv(csv_path: str,timeout:int=15):
    try:
        print('waiting')
        with portalocker.Lock(csv_path, mode='r+',newline='',timeout=timeout,fail_when_locked=False, flags=portalocker.LOCK_EX | portalocker.LOCK_NB) as locked_file:
            df = pd.read_csv(locked_file,na_values=['<NA>'])
            print('reading')
            print(df)
            df = pd.concat([df,pd.DataFrame({'a':[8],'b':[8]})],ignore_index=True)
            print('writing')
            print(df)
            locked_file.seek(0) #ย้าย cursor ไปส่วนต้นของ file
            locked_file.truncate(0)  # 🔥 ลบเนื้อหาทั้งหมดของไฟล์
            df.to_csv(locked_file,na_rep='<NA>',index=False,mode='w')
            import time
            locked_file.seek(0) #ย้าย cursor ไปส่วนต้นของ file
            df = pd.read_csv(locked_file,na_values=['<NA>'])
            print('reading update')
            print(df)
            time.sleep(10)
            print('ok')
    except portalocker.exceptions.LockException as e:
        print(f"portalocker.exceptions.LockException : timeout : {timeout} : {e}")
    except Exception as e:
        print(f"Exception : {e}")

if __name__=='__main__':
    safe_update_dataframe_to_csv('./2_test_csv.csv')