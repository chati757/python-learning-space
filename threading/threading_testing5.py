import threading
 
class FuncThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)
 
    def run(self):
        self._target(*self._args)
 
# Example usage
def someOtherFunc(data,key,text):
    print "someOtherFunc was called : data=%s; key=%s" % (str(data), str(key))
    print(text)
 
t1 = FuncThread(someOtherFunc,[1,2], 6,"test")
t1.start()
t1.join()

'''
someOtherFunc was called : data=[1, 2]; key=6
test
'''