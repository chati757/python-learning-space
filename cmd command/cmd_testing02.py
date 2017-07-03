import subprocess

def showtxt(txt):
    print(txt)
    print("ok")

def simple_cmd(command):
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    teststr= proc.stdout.read()
    showtxt(teststr)

if __name__=="__main__":
    simple_cmd("dir")