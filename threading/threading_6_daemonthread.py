import threading 

#join function it'dose wait the current thread terminated before to do create new thread
def do_this():
    global count

    print("this first thread!")
    while(count<300):
        count+=1
        pass
        
    print(count)
    
def do_after():
    global count
    
    print("this second thread!")
    while(count<300):
        count+=1
        pass

def main():
    global count
    count = 0

    #by raw main thread is not daemon = false
    main_thread=threading.enumerate()[0]
    print(main_thread.isDaemon())#false becase it's not daemon

    our_next_thread=threading.Thread(target=do_after)
    our_next_thread.start()
    print(next_thread.isDaemon())#false

    # daemon thread ตามกฏของ python python จะออกจากโปรแกรมก็ต่อเมื่อ daemon 


if(__name__=="__main__"):
    main()