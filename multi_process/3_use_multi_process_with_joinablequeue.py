from multiprocessing import Process, JoinableQueue
from queue import Empty
import time


def consumer(que, pid ,t):
    while True:
        try:
            item = que.get(timeout=10)
            print("%s consume:%s" % (pid, item))
            time.sleep(t)
            que.task_done() #que จะไม่ join ถ้า task_done() ไม่ครบ 10 ครั้งตาม queue ที่เข้ามา
        except Empty:
            print('is empty')
            break
    print('Consumer done')


def producer(sequence, que):
    for item in sequence:
        print('produce:', item)
        que.put(item) 
        time.sleep(1)

if __name__ == '__main__':
    que = JoinableQueue()

    # create two consumer process
    cons_p1 = Process(target=consumer, args=(que, 1 , 2)) 
    cons_p1.start() 
    cons_p2 = Process(target=consumer, args=(que, 2 , 0))
    cons_p2.start() 

    sequence = [i for i in range(10)]
    producer(sequence, que)
    
    print('waiting que join')
    que.join()
    print('waiting cons join')
    cons_p1.join()
    cons_p2.join()