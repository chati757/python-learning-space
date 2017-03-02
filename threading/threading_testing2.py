import threading
import time 

class AsyncWrite(threading.Thread):
    def __init__(self,text,out):
            threading.Thread.__init__(self) 
            self.text = text
            self.out = out

    def run(self):
        f=open(self.out,"a")
        f.write(self.text+'\n')
        f.close()
        time.sleep(2)
        print("Finished Background File Write to "+self.out)

def Main():
    message = raw_input("Enter a string to store:")
    background = AsyncWrite(message,'test.txt')
    background.start()
    print("The program can continue while it writes in another thread")
    print("100 + 400= ",100+400)
    
    print("now waiting thread working")
    background.join() # when thread finised and join this line to be continue print line 26.
    print("Waited until thread was complete")

if __name__ == '__main__':
 Main()