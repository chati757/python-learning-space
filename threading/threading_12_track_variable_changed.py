import threading
import time

class track_data_change:
    def __init__(self):
        self._value = 0
        self._value_changed = threading.Event()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        print('insetter')
        self._value = new_value
        self._value_changed.set()
        print('notify complete')

def thread_function(data):
    while True:
        data.value += 1
        print("Thread 1: Data changed to", data.value)
        time.sleep(2)  # รอเวลาผ่านไป 2 วินาที

if __name__ == "__main__":
    data = track_data_change()
    
    # สร้างและเริ่มต้น thread 1
    thread1 = threading.Thread(target=thread_function, args=(data,))
    thread1.setDaemon(True)
    thread1.start()

    # main thread เป็น listener ที่ตรวจจับการเปลี่ยนแปลงของตัวแปร
    x = 0
    while(x<5):
        x+=1
        print("Main Thread: Waiting for data change...")
        data._value_changed.wait()
        print(f"Main Thread: Data changed to : {data.value}")
        print('----------')
        data._value_changed.clear()  # รีเซ็ตสถานะของ Event
    
    print('EOF')