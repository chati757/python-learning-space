import os
import threading
import subprocess

class execCmd(threading.Thread): 
    def __init__(self,cmd_data):
        threading.Thread.__init__(self)
        self.command = cmd_data
        self.output = None
        self.daemon = True

    def run(self):
        try:
            proc = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            self.output = proc.stdout.read()
            self.output += proc.stderr.read() 
        except Exception as e:
            #if verbose == True: print_exc()
            pass
'''
def showtxt(txt):
    print(txt)
    print("ok")

def simple_cmd(command):
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    teststr= proc.stdout.read()
    showtxt(teststr)
'''
if __name__=='__main__':
    #simple_cmd('tasklist')
    background = execCmd('dir c:')
    background.start()
    print("now waiting thread working")
    background.join() # when thread finised and join this line to be continue print line 26.
    print("Waited until thread was complete")
    print("result :")
    print background.output
    print("total characters")
    print len(background.output)
    print("check thread :")
    print threading.active_count()
    print threading.enumerate()
    