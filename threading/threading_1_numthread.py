import threading 

def main():
    print(threading.active_count()) #1
    print(threading.enumerate())#show all thread actually running  
    print(threading.current_thread())#show current thread is running

    #thread is like a procress
    
if(__name__=="__main__"):
    main()