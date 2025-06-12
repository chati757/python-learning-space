import threading
import time

class custom_class_thread(threading.Thread):
    def __init__(self):
        super(custom_class_thread, self).__init__()
        self.setDaemon(True)
        self.global_tracking_data = 0
    
    def run(self):
        self.testchange_global()

    def testchange_global(self):
        time.sleep(3)
        print('intestchange_global')
        self.global_tracking_data = 1

if __name__ == '__main__':
    fsdt = custom_class_thread()
    fsdt.start()

    print('main thread running')
    x = 0
    while x < 10:
        x += 1
        time.sleep(1)
        print(fsdt.global_tracking_data)

    print('stop')