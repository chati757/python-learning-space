import multiprocessing as mp
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import tkinter as tk
from tkinter import simpledialog

rt = tk.Tk()
rt.withdraw()

global_logging_dict_df = {
    'ptt':pd.DataFrame({'date':[0,1,2],'bid1':[15.3,15.2,15.1],'offer1':[15.4,15.3,15.2]}),
    'aot':pd.DataFrame({'date':[0,1,2],'bid1':[26.25,26.00,26.25],'offer1':[26.50,26.25,26.50]})
}

global_plot_register = {}

class graph:
    #constructor 
    #ex gender = famale < it's class variable
    def __init__(self,symbol):
        #slef name < it's instance variable
        self.symbol = symbol
        self.fig, self.ax = plt.subplots()
        self.x = global_logging_dict_df[self.symbol]['date']
        self.y = global_logging_dict_df[self.symbol]['bid1']
        self.ax.plot(self.x, self.y, 'ro')
        self.sender_pipe,self.thread_receiver_pipe = mp.Pipe()
        self.plot_process = mp.Process(target=self._process_assign_task_and_alive_on_show, daemon=True)
        self.plot_process.start()
        print(f'{self.symbol} : processing id : {self.plot_process.pid}')

    def _process_assign_task_and_alive_on_show(self): #using protect instead of private because private function cannot call from another process
        #regist to close event
        self.fig.canvas.mpl_connect('close_event', self.__on_close)
        #release graph timer thread to auto_flushing and listening data comming
        timer = self.fig.canvas.new_timer(interval=500)
        timer.add_callback(self.__thread_auto_flush_and_listener)
        print(f'{self.symbol}:assign task for thread')
        timer.start()
        print(f'{self.symbol}:living on show')
        plt.show() #process alive on this
        print(f'{self.symbol}:exit from show')

    def __thread_auto_flush_and_listener(self):
        while self.thread_receiver_pipe.poll():
            user_minvol_input = simpledialog.askinteger(title=f'book_val_graph',prompt="ENTER MINIMUM VOL. LIMIT | K.unit")
            data = self.thread_receiver_pipe.recv()
            if(data=='close'):
                print('receive close sig.')
                break
            self.x.loc[len(self.x)] = data[0]
            self.y.loc[len(self.y)] = data[1]
            self.ax.plot(self.x, self.y, 'ro')
            self.fig.canvas.draw_idle()

    def __on_close(self,event):
        print(f'{self.symbol} : on close event : sending close sig to listener')
        self.sender_pipe.send('close')

    def send_plot(self,y):
        try:
            self.sender_pipe.send([self.x.iloc[-1]+1,y])
        except IndexError:
            self.sender_pipe.send([0,y])

if __name__=='__main__':
    global_plot_register['ptt'] = graph('ptt')
    print('waiting for plot')
    time.sleep(10)
    global_plot_register['ptt'].send_plot(15.5)
    time.sleep(4)