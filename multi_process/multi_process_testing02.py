import os
from multiprocessing import Process , Pipe
import time

def ponger(p,s):
    count = 0
    while count < 5:
        msg = p.recv()#wait msg
        print(count)
        print(os.getpid())
        print(msg)
        time.sleep(1)
        p.send(s)
        count +=1

if __name__ == "__main__":
    parent , child = Pipe()
    #--------procress [02]--------------
    proc = Process(target=ponger,args=(child,"pong"))
    proc.start()
    #--------procress [01]--------------
    parent.send("ping")
    ponger(parent,"ping")
    #import pdb;pdb.set_trace()
    #proc.join()

    '''
    check tasklist it's have 2 procress communicate together
    '''