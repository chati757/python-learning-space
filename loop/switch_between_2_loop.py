import time
from datetime import datetime
import threading

'''
ทดสอบ switch loop ของ main ด้วย sub-thread
โดย mainloop ทำงานปกติและรอการส่ง data จาก sub-thread ไปด้วย
เมื่อ data ของ sub-thread เข้ามา 'data is comming' 
main-process และ main-thread จะ
เป็นคนทำงาน do something
'''

data_coming_state = False

def check_state():
    global data_coming_state
    print('prepare to receive')
    time.sleep(20)
    data_coming_state = True

receiver_thread = threading.Thread(target=check_state,daemon=True).start()

def do_another_and_back(delay=5):
    global data_coming_state
    buff_sec = round(delay,0)
    buff_microsec = delay-buff_sec
    print(buff_sec)
    print(buff_microsec)
    buff_start_sec = 1
    while (buff_start_sec<=buff_sec):
        print(f'{buff_start_sec}/{buff_sec}')
        print(data_coming_state)
        buff_start_sec+=1
        if(data_coming_state==True):
            print('data is comming')
            print('do someting')
            data_coming_state=False
        time.sleep(1)

    if(buff_microsec>0):
        time.sleep(buff_microsec)

while True:
    print('inmain loop')
    buff_current_time = datetime.now()
    #second loop
    do_another_and_back(delay=(60 - (buff_current_time.second + buff_current_time.microsecond/1000000.0)))


receiver_thread.join()
print('ending')