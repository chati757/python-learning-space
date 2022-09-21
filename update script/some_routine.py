import threading
import time

share_num = 1

share_data_obj = {
    'data1':'testdata1',
    'data2':'testdata2'
}

def loop():
    global share_num
    while True:
        time.sleep(1)
        share_num += 2

threading.Thread(target=loop,daemon=True).start()
