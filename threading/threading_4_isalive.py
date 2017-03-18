import threading 

def do_this():
    global dead
    count = 0

    print("this os our thread!")
    while(not dead):
        count+=1
        pass
        
    print(count)
    
def main():
    global dead
    dead = False
    #threading.Thread(target=function)
    our_thread = threading.Thread(target=do_this,name=ourthread)
    our_thread.start()#seperate procress

    print(threading.active_count()) #1
    print(threading.enumerate())#show all thread actually running  
    print(our_thread.is_alive())

    #thread is like a procress
    #enumerate display different case 1 [thread1,thread2] case 2 [thread1] case3 [thread2]
    #sometime can do function do_this sometime not do function do_this
    #**if some thread is end, the all thread is stop .for example maybe thread 1 end first and thread 2 is stop! in that time

    raw_input("hit enter to thread die:")
    dead = True
    #*sometime the our_thread is die after check in is_alive() function. and thread 1 instead print our_thread.is_alive 
    #print(our_thread.is_alive()) # it get true and false
    raw_input("the our thread has died wait a bit and hit enter again:")
    print(our_thread.is_alive())#it get false only
    print(threading.active_count()) #1
    print(threading.enumerate())#show all thread actually running  


if(__name__=="__main__"):
    main()