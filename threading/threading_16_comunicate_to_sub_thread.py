import threading
import time

class test_thread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.count = 0
    
    def run(self):
        while self.count==0:
            time.sleep(1)
            print('working..')

        print('go out from loop')

if __name__=='__main__':
    tt = test_thread()
    tt.start()

    time.sleep(5)
    tt.count = 1 #change self.count in sub-thread from 0 to 1
    time.sleep(2)

    print(threading.enumerate())
    import pdb;pdb.set_trace()