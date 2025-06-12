import threading
import os
import time

class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._event = threading.Event()

    def run(self):
        print('prepare something before available some_sevice function')
        time.sleep(10)
        self._event.set()

    def some_service(self):
        self._event.wait()
        print('do some service')

    def stop(self):
        print("Stopping thread...")
        self._event.clear()

    def stop_and_join(self):
        self.stop()
        self.join()

# การใช้งาน
my_thread = MyThread()
my_thread.start()

'''
เมื่อเรียกใช้ my_thread เร็วเกินไป self._event.wait() จะสั่งให้รอจนกว่า my_thread จะเตรียม
บางอย่างเสร็จ เมื่อ my_thread เตรียมเสร็จ my_thread จะสั่ง self._event.set() เพื่อเป็นการบอกให้หยุดรอได้
และ function some_service ได้พร้อมให้บริการแล้ว และในครั้งถัดๆไปก็ไม่ต้องรอแล้วสามารถเรียกใช้ได้เลย
'''
print('wait prepare MyThread in firsttime')
my_thread.some_service()

print('do some service nexttime')
my_thread.some_service()
my_thread.some_service()

my_thread.stop_and_join()

print("Main thread finished")