#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psutil
import threading
import time

lock = threading.Lock()

class some_class():
    def __init__(self):
        print('in init')
        
    def do_this(self,df,someglobal):
        with lock:
            x = 0
            print(f'insert:{str(threading.current_thread())} to {someglobal}')
            someglobal.append(str(threading.current_thread()))
            print(someglobal)
            while(x<10):
                x+=1
                print(f'do this with : {threading.current_thread()}')
                time.sleep(1)
            
            return df

def task(para,log_thread):
    sc = some_class()
    sc.do_this(para,log_thread)

if(__name__=="__main__"):
    global log_thread
    log_thread = []
    print('main running')
    print(f"mainthread pid : {psutil.Process().pid}")

    our_thread = threading.Thread(target=task,args=(1,log_thread,))
    our_thread.setDaemon(True)

    our_next_thread = threading.Thread(target=task,args=(2,log_thread,))
    our_next_thread.setDaemon(True)

    our_thread.start()
    our_next_thread.start()
    
    x = 0
    while(x<30):
        x+=1
        print(f'main logging : {log_thread}')
        time.sleep(1)

    our_thread.join()
    our_next_thread.join()
    print('end')

