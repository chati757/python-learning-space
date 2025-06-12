# -*- coding: utf-8 -*-

import os
import pandas as pd
import portalocker

'''
#flags=portalocker.LOCK_EX | portalocker.LOCK_NB
#มีความหมายว่า ให้ใช้ share_lock (สำหรับ write [lock ได้ทีละ process ไม่สามารถ lock หลาย process พร้อมกัน]) แต่หากเจอว่า share lock หรือ exclusive lock จะต้องรอ แต่เป็นการรอแบบ lock_nb คือรอแบบ non-block โดยมี timeoutเมื่อรอเป็นระยะเวลานึงจะ non-block และ raise
'''

def safe_append_dataframe_to_csv(df: pd.DataFrame, csv_path: str,timeout:int=15):
    try:
        print('waiting')
        with portalocker.Lock(csv_path, mode='a',newline='',timeout=timeout,fail_when_locked=False, flags=portalocker.LOCK_EX | portalocker.LOCK_NB) as locked_file:
            df.to_csv(locked_file,na_rep='<NA>',index=False,mode='a',header=(not os.path.exists(csv_path)))
            import time
            print('apending')
            time.sleep(10)
            print('ok')
    except portalocker.exceptions.LockException as e:
        print(f"portalocker.exceptions.LockException : timeout : {timeout} : {e}")
    except Exception as e:
        print(f"Exception : {e}")

if __name__=='__main__':
    df = pd.DataFrame({'a':[9,None],'b':[None,9]})
    safe_append_dataframe_to_csv(df,'./2_test_csv.csv')