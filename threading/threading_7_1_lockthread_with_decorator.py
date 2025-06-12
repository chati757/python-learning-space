#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psutil
import threading
import time

global lock,log_thread
log_thread = []
lock = threading.Lock()#เมื่อเราใส่ lock ให้ function มันจะไม่โดน thread อื่นแทรกระหว่าง thread นั้นกำลังทำงาน function นั้นอยู่
#ตัวอย่างเช่น thread a ทำ function do_this() thread b จะทำ do_this() ณ ตอนนั้นไม่ได้จนว่า thread a จะทำเสร็จและ release lock ออก

def lock_thread_decorator(original_function):
    print('lock_thread_decorator func')
    print('  do another before call '+original_function.__name__+'()')
    def wrap_function(*arg):
        global lock
        print(f'\nlock acquire with : {threading.current_thread()}')
        lock.acquire()
        print('  wrap func')
        print('    check arg of '+original_function.__name__+'()')
        print('    call original function '+original_function.__name__+'()')
        def do_after(result_of_func):
            global lock
            print(f'do_after lock release : {threading.current_thread()}')
            lock.release()
            return result_of_func
        return do_after(original_function(*arg))
    return wrap_function

@lock_thread_decorator
def do_this(df):
    global log_thread
    x = 0
    log_thread.append(str(threading.current_thread()))
    while(x<10):
        x+=1
        print(f'do this with : {threading.current_thread()}')
        time.sleep(1)
    
    return df

def main():
    print('main running')
    print(f"mainthread pid : {psutil.Process().pid}")

    our_thread = threading.Thread(target=do_this,args=(1,))
    our_thread.setDaemon(True)

    our_next_thread = threading.Thread(target=do_this,args=(2,))
    our_next_thread.setDaemon(True)

    our_thread.start()
    our_next_thread.start()
    print("enumerate ",threading.enumerate())
    our_thread.join()
    our_next_thread.join()
    
    print('\ndo with main thread after join')
    import pandas as pd
    df = pd.DataFrame({'a':[2,3,4],'b':[2,3,4]})
    print(do_this(df))
    global log_thread
    print(log_thread)
    input("\npress enter to kill every thread ")

if(__name__=="__main__"):
    main()
