import time

def fucone(name):
    print("name is "+name)

def test():
    global buf
    buf = 5

def test2(disp_log=False):
    i=0
    while 1:
        i+=1
        if(disp_log==True):
            #print(str(i).strip('\n\r'))
            time.sleep(1)
            print("run"+str(i),end='\r')
        if(i>=5):
            print("in break")
            break

#array passing
arr = [1,4,5]
def test3(arr):
    print(arr)

if __name__=="__main__":
    fucone("test")
    #test()
    #print(buf)
    
    test2(disp_log=True)
    #testval="test0"
    #print(testval.strip('0'))


