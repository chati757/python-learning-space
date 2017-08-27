#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

    #by raw main thread is not daemon = false
    our_thread = threading.Thread(target=do_this)
    our_thread.setDaemon(True)# true จะทำให้ loop while หยุดเมื่อ main thread ทำบรรทัด 28 เสร็จ
    our_thread.start()#seperate procress


    print("daemon ",our_thread.isDaemon())
    print("count ",threading.active_count())
    print("enumerate ",threading.enumerate())

    raw_input("hit enter to thread die:")

    print("last line stop deamon")

    # daemon จะถูก set เบื่องต้นเป็น false ทุก thread
    # daemon thread = true ตามกฏของ python python จะออกจากโปรแกรมก็ต่อเมื่อ non-daemon(main thread) ทำงานจบ
    # จุดประสงค์ของ daemon boolean คือบอกว่า มันโดนสร้างมาแบบไหนถ้า thread โดนสร้างมากจาก main thread daemon จะเป็น false
    # แต่ถ้า thread ไม่ได้สร้าง จาก main thread แต่ถูกสร้างจาก thread ธรรมดามันจะเป็น true 

if(__name__=="__main__"):
    main()