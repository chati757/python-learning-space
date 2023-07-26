import multiprocessing as mp
import time

def job(a):
    print("injob")
    for i in range(1,4):
        time.sleep(1)
        print(100*a+i)

if(__name__=='__main__'):
    pool = mp.Pool(processes=2)
    for j in range(1,6):
        pool.apply_async(job,(j,))
    
    pool.close() #close pool after no use pool anymore
    pool.join() #check all workers were terminated (synchronization point)
    print('end')