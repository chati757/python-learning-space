import tkinter as tk
from tkinter import simpledialog
import win32gui
import win32con
import multiprocessing as mp
import threading
import matplotlib.pyplot as plt
import numpy as np 
import time

def focus_window(title):
    time.sleep(0.3)
    hwnd = win32gui.FindWindow(None, title)
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
    else:
        print("Window with title '{}' not found!".format(title))

rt = tk.Tk()
rt.withdraw()
rt.geometry('0x0+400+200')
rt.update_idletasks()
# Create the main window
class test:
    def __init__(self):
        self.x = np.array([1,4,5])
        self.y = np.array([0,0.4,-0.4])
        self.fig = plt.figure(figsize=[6,6],dpi=100)
        self.fig.subplots_adjust(0.125,0.095,0.95,0.95,0.35,0.35)
        self.ax1 = self.fig.gca()
        self.ax1.plot(self.x,self.y,'g')

        self.plot_process = mp.Process(target=self.show_graph, daemon=True)
        self.plot_process.start()

    def show_graph(self):
        self.fig.canvas.mpl_connect('key_press_event',self.on_press)
        plt.show()

    def on_press(self,event):
        print('on_press')
        if(event.key=='1'):
            threading.Thread(target=focus_window,args=(f'book_val_graph : test',),daemon=True).start()
            self.user_date_input = simpledialog.askstring(title=f'book_val_graph : test',prompt="ENTER DATE | format YYYYMMDD\t\t\t",parent=rt)

        elif(event.key=='2'):
            threading.Thread(target=focus_window,args=(f'book_val_graph : test',),daemon=True).start()
            self.user_num_input = simpledialog.askinteger(title=f'book_val_graph : test',prompt="ENTER DATE | format YYYYMMDD\t\t\t",parent=rt)
        
        print(threading.enumerate())
    
if __name__ == "__main__":
    test()
    import time
    time.sleep(10)