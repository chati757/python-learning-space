import threading
import Queue

cmdqueue = Queue.Queue() # create queue object
#--------------------------------worker structure------------------------------------------
def workerThread(queobject):
     while True:
          vars = queobject.get()
          print vars
          queobject.task_done()
#--------------------------------create worker 4 worker------------------------------------
for i in range(4):
     worker = threading.Thread(target=workerThread, args=(cmdqueue,))
     worker.setDaemon(True)#protect for zombie threads
     '''
     main thread is not daemon and All thread when we create in main 
     the daemon thread default is set(False) when we build main thread.
     if daemon thread is created in thread it's must to be set(True)
     
     '''
     worker.start()
#--------------------------------put queue-------------------------------------------------
for i in range(5):
     data = {
          'id': i,
     }
     cmdqueue.put(data)
cmdqueue.join()
#------------------------------------------------------------------------------------------