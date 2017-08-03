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
    our_thread = threading.Thread(target=do_this,name="testing thread")
    our_thread.start()#seperate procress

    print(threading.active_count()) #1
    print(threading.enumerate())#show all thread actually running  
    #print(threading.current_thread())#show current thread is running

    #thread is like a procress
    #enumerate display different case 1 [thread1,thread2] case 2 [thread1] case3 [thread2]
    #sometime can do function do_this sometime not do function do_this
    #**if some thread is end, the all thread is stop .for example maybe thread 1 end first and thread 2 is stop! in that time

    input("hit enter to thread die:")
    dead = True
if(__name__=="__main__"):
    main()