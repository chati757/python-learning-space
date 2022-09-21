#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time

global lock,x
x=0
lock = threading.Lock()#เมื่อเราใส่ lock ให้ function มันจะไม่โดน thread อื่นแทรกระหว่าง thread นั้นกำลังทำงาน function นั้นอยู่
#ตัวอย่างเช่น thread a ทำ function do_this() thread b จะทำ do_this() ณ ตอนนั้นไม่ได้จนว่า thread a จะทำเสร็จและ release lock ออก

def lock_thread_decorator(original_function):
    print('lock_thread_decorator func')
    print('  do another before call '+original_function.__name__+'()')
    def wrap_function(*arg):
        global lock
        print('lock acquire')
        lock.acquire()
        print('  wrap func')
        print('    check arg of '+original_function.__name__+'()')
        print('    call original function '+original_function.__name__+'()')
        def do_after(result_of_func):
            global lock
            print('do_after lock release')
            lock.release()
            return result_of_func
        return do_after(original_function(*arg))
    return wrap_function

@lock_thread_decorator
def do_this(df):
    global x,lock

    while(x<10):
        x+=1
        print('do this')
        time.sleep(1)
    
    return df


def main():
    print('main running')
    '''
    our_thread = threading.Thread(target=do_this)
    our_thread.start()

    our_next_thread = threading.Thread(target=do_this)
    our_next_thread.start()

    our_thread.join()
    our_next_thread.join()
    '''
    print('with main thread')
    import pandas as pd
    df = pd.DataFrame({'a':[2,3,4],'b':[2,3,4]})
    print(do_this(df))

if(__name__=="__main__"):
    main()
