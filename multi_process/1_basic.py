import time
import multiprocessing as mp

def job(a):
    for i in range(2):
        time.sleep(2)
        print('งานที่ %d รอบที่ %d'%(a,i+1))

if(__name__=='__main__'):
    #create and start multi process
    process_registor = []
    for j in range(4):
        p = mp.Process(target=job,args=(j+1,))
        p.start()
        process_registor.append(p)
    print('เริ่มงานได้แล้ว')

    #end multi process
    for p in process_registor:
        p.join()
    print('เก็บกวาดหลังเลิกงาน')