# -*- coding: utf-8 -*-

import pandas as pd
import portalocker

'''
flags=portalocker.LOCK_SH | portalocker.LOCK_NB
มีความหมายว่า ให้ใช้ share_lock (สำหรับ read [lock พร้อมกันหลาย process ได้]) แต่หากเจอว่า exclusive lock จะต้องรอ แต่เป็นการรอแบบ lock_nb คือรอแบบ non-block โดยมี timeoutเมื่อรอเป็นระยะเวลานึงจะ non-block และ raise
'''

def safe_read_csv_to_dataframe(df: pd.DataFrame, csv_path: str,timeout:int=15):
    try:
        print('waiting')
        with portalocker.Lock(csv_path, mode='r',newline='',timeout=timeout,fail_when_locked=False, flags=portalocker.LOCK_SH | portalocker.LOCK_NB) as locked_file:
            df = pd.read_csv(locked_file,na_values=['<NA>'])
            import time
            print('reading')
            time.sleep(10)
            print(df)
            print('ok')
    except portalocker.exceptions.LockException as e:
        print(f"portalocker.exceptions.LockException : timeout : {timeout} : {e}")
    except Exception as e:
        print(f"Exception : {e}")

if __name__=='__main__':
    df = pd.DataFrame({'a':[2,3,4,None],'b':[4,5,None,8]})
    safe_read_csv_to_dataframe(df,'./2_test_csv.csv')