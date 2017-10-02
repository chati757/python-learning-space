import threading
import queue
import time

cmdqueue = queue.Queue() # create queue object
#--------------------------------worker structure------------------------------------------
def workerThread(queobject,thread_id):
     while True:
        print("[",thread_id,"]worker wait queue")    
        vars = queobject.get()
        if(vars==None):
            print("[",thread_id,"]break")   
            break  
        print("[",thread_id,"]",vars)
        queobject.task_done() # for thread tell queue is this thread is done
        print("[",thread_id,"]task_done")
#--------------------------------create worker 4 worker------------------------------------
thread_id=0
threads=[]
for i in range(4):
    thread_id+=1
    worker = threading.Thread(target=workerThread, args=(cmdqueue,thread_id,))
    worker.setDaemon(True)#protect for zombie threads
    '''
    main thread is not daemon and All thread when we create in main 
    the daemon thread default is set(False) when we build main thread.
    if daemon thread is created in thread it's must to be set(True)

    '''
    worker.start()
    threads.append(worker)
#--------------------------------put queue-------------------------------------------------
for i in range(10):
    #time.sleep(2)
    data = i
    cmdqueue.put(data)
    
cmdqueue.join() # block until all tasks are done

print("stop worker")
# stop workers
for i in range(4):
    cmdqueue.put(None)

for t in threads:
    t.join()
print("end of main thread")
#------------------------------------------------------------------------------------------