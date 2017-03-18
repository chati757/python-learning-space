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

    our_thread=threading.Thread(target=do_this)
    our_thread.start()
    our_thread.join() #wait thread 1 terminite first if want to know different delete this line and run
    our_next_thread=threading.Thread(target=do_after)
    our_next_thread.start()


if(__name__=="__main__"):
    main()