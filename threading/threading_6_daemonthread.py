#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psutil
import threading 
import time


def do_this():
    global dead
    count = 0

    print("this os our thread!")
    while(not dead):
        count+=1
        time.sleep(2)
        print("count func",count)
        pass

def main():
    global dead
    dead = False

    print(f"mainthread pid : {psutil.Process().pid}")

    #by raw main thread is not daemon = false
    our_thread = threading.Thread(target=do_this)
    print(f'defualt our_thread daemon is : {our_thread.isDaemon()}')
    our_thread.setDaemon(True)# true จะทำให้ loop while หยุดเมื่อ main thread ทำบรรทัด print("last line stop deamon") เสร็จ
    our_thread.start()#seperate procress

    print("daemon ",our_thread.isDaemon())
    print("count ",threading.active_count())
    print("enumerate ",threading.enumerate())

    input("hit enter to thread die:")

    print("last line stop deamon")

    # daemon จะถูก set เบื่องต้นเป็น false ทุก thread
    # daemon thread = true ตามกฏของ python python จะออกจากโปรแกรมก็ต่อเมื่อ non-daemon(main thread) ทำงานจบ
    # จุดประสงค์ของ daemon boolean คือบอกว่า มันโดนสร้างมาแบบไหนถ้า thread เป็น main thread daemon จะเป็น false
    # แต่ถ้า thread ไม่ได้เป็น main thread แต่เป็น thread ที่ถูกสร้างมาทีหลัง ปกติมันจะเป็น true 

if(__name__=="__main__"):
    main()