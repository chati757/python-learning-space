import multiprocessing as mp
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.lines as lines
import matplotlib.ticker as ticker
import win32gui
import win32con
import pandas as pd
import numpy as np
from matplotlib import rcParams
from datetime import datetime
from datetime import timedelta
from matplotlib.widgets import Button
from matplotlib.widgets import TextBox
import tkinter as tk
from tkinter import simpledialog
import threading
import ctypes #for alertbox
import os
import time

#prepare to dialog box when press key binding
rt = tk.Tk()
rt.withdraw()
rt.geometry('0x0+400+200')
rt.update_idletasks()

global_buffer_serie = {} #for ax2
global_logging_dict_df = {} #global variable of time_machine , for ax1
global_time_prototype_df = pd.read_csv("./logging_csv/time_prototype.csv",index_col=False)

rcParams['axes.unicode_minus'] = False 
plt.rc('font',family='White Rabbit')
#rcParams['toolbar'] = 'None'

class cross_hair_cursor:
    def __init__(self,ax):
        self.ax = ax
        self.background = None
        self.default_color = '#F2E2AC'
        self.horizontal_line = ax.axhline(color=self.default_color, lw=1, ls='-')
        self.vertical_line = ax.axvline(color=self.default_color, lw=1, ls='-')
        self._creating_background = False
        self.ax.figure.canvas.mpl_connect('draw_event', self.on_draw)
        self.ax.figure.canvas.draw()
    
    def on_draw(self,event):
        self.create_new_background()
    
    def set_cross_hair_visible(self, visible):
        need_redraw = self.horizontal_line.get_visible() != visible
        self.horizontal_line.set_visible(visible)
        self.vertical_line.set_visible(visible)
        return need_redraw
    
    def create_new_background(self):
        if self._creating_background:
            # discard calls triggered from within this function (from self.ax.figure.canvas.draw() function)
            return
        self._creating_background = True
        self.set_cross_hair_visible(False)
        self.ax.figure.canvas.draw()

        self.background = self.ax.figure.canvas.copy_from_bbox(self.ax.bbox)
        self._creating_background = False
    
    def on_mouse_move(self, event):
        if self.background is None:
            self.create_new_background()

        if not event.inaxes:
            need_redraw = self.set_cross_hair_visible(False)
            if need_redraw:
                self.ax.figure.canvas.restore_region(self.background)
                self.ax.figure.canvas.blit(self.ax.bbox)
        elif(event.inaxes.get_title()==self.ax.get_title()):
            self.set_cross_hair_visible(True)
            # update the line positions
            x, y = event.xdata, event.ydata
            self.horizontal_line.set_ydata(y)
            self.vertical_line.set_xdata(x)

            self.ax.figure.canvas.restore_region(self.background)
            self.ax.draw_artist(self.horizontal_line)
            self.ax.draw_artist(self.vertical_line)
            self.ax.figure.canvas.blit(self.ax.bbox)

def focus_window(window_title):
    time.sleep(0.3)
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
    else:
        print("Window with title '{}' not found!".format(window_title))

def price_range(price):
    if(price < 0):
        raise Exception('price is negative value')

    pos = None
    result_price = None
    price_level = [2,5,10,25,100,200,400,600] #price >= 600 recognize to index
    price_range_result = [0.01,0.02,0.05,0.1,0.25,0.5,1,2,1] #price >= 400 is 2

    for c,i in enumerate(price_level):
        if(price < i):
            pos = c
            break
        if(c==(len(price_level)-1) and pos == None):
            pos = len(price_level)

    result_price = price_range_result[pos]

    return result_price

class bookvol_graph:
    def __init__(self,symbol):
        self.symbol = symbol
        self.fig_width = 7
        self.fig_height = 5
        self.bgcolor = "#293058"
        self.color = "#F1F0F9"
        self.upcolor = "#E2FF82"
        self.downcolor = "#FC69AB"
        self.bookvol_date_str_buff = 't-0'
        self.last_file_date_str = None
        self.date_range_str_list = None
        self.time_prototype_df = pd.read_csv("./logging_csv/time_prototype.csv",index_col=False)
        self.bookvol_df_buff = None
        self.bookvol_axis_status = None
        self.start_bookvol_datetime = None
        self.end_bookvol_datetime = None
        self.candle_se_buff = None
        self.symbol_hist_df = None #for extract candle_se_buff and check in press_key_prev
        self.candle_axis_status = None
        self.minlim_vol_filter = 200 #unit is K.

        self.config_figure()
        self.config_axis_bookvol()
        self.config_axis_candle()
        self.select_bookvol_dataframe_by_date(self.bookvol_date_str_buff) #draw txt if 'not found' or 'wait'
        self.select_candle_dataframe_by_date(self.bookvol_date_str_buff) #draw txt if 'not found' or 'wait'

        if(isinstance(self.bookvol_df_buff,pd.DataFrame)==True):
            self.normalize_bookvol_dataframe() #normalize and repair incomplate self.bookvol_df_buff
            self.plot_to_bookvol_axis()
            self.set_scale_bookvol_axis()
        
        if(isinstance(self.candle_se_buff,pd.Series)==True):
            self.plot_to_candle_axis()
            self.set_scale_candle_axis()

        self.fig.canvas.draw_idle() #draw plot data
        self.sender_pipe,self.thread_receiver_pipe = mp.Pipe()
        self.plot_process = mp.Process(target=self._process_assign_task_and_alive_on_show, daemon=True)
        self.plot_process.start()

    #config figure
    def config_figure(self):
        self.fig = plt.figure(figsize=[self.fig_width,self.fig_height],tight_layout=False,dpi=100,facecolor=self.bgcolor)
        self.mgs = self.fig.add_gridspec(nrows=1,ncols=1)
        self.sgs1 = self.mgs[0].subgridspec(nrows=16,ncols=16,wspace=1,hspace=1)

    def config_binding_keyboard(self):
        self.fig.canvas.mpl_connect('key_press_event', self.binding_keyboard_event)

    #binding keyboard function
    def binding_keyboard_event(self,event):
        if(event.key=='1'):
            self.press_key_prev()
        elif(event.key=='2'):
            self.press_key_next()
        elif(event.key=='3'):
            self.press_key_jump_to_date()
        elif(event.key=='4'):
            self.press_key_set_min_vol()

    def press_key_next(self):
        if(self.bookvol_date_str_buff!='t-0'):
            if(self.bookvol_date_str_buff==datetime.strftime(datetime.now(),"%Y-%m-%d")):
                self.bookvol_date_str_buff = 't-0'
                self.send_request_logging_df()
            else:
                if(self.date_range_str_list==None):
                    sorted_logging_csv_date_se = pd.Series([datetime.strptime(i.replace(".csv",""),"%Y%m%d") for i in os.listdir(f"./logging_csv/{self.symbol}.bk")]).sort_values()
                    self.date_range_str_list = sorted_logging_csv_date_se[sorted_logging_csv_date_se!=datetime(*datetime.now().date().timetuple()[:6])].dt.strftime("%Y-%m-%d").tolist()

                if(self.bookvol_date_str_buff == self.date_range_str_list[-1]):
                    self.bookvol_date_str_buff = 't-0'
                    self.send_request_logging_df()
                else:
                    self.bookvol_date_str_buff = self.date_range_str_list[self.date_range_str_list.index(self.bookvol_date_str_buff)+1]
            
                    self.select_bookvol_dataframe_by_date(self.bookvol_date_str_buff)
                    self.select_candle_dataframe_by_date(self.bookvol_date_str_buff)

                    if(isinstance(self.bookvol_df_buff,pd.DataFrame)==True):
                        self.normalize_bookvol_dataframe()
                        self.plot_to_bookvol_axis()
                        self.set_scale_bookvol_axis()

                    if(isinstance(self.candle_se_buff,pd.Series)==True):
                        self.plot_to_candle_axis()
                        self.set_scale_candle_axis()

                    self.fig.canvas.draw_idle() #draw plot data
        '''
        if(self.bookvol_date_str_buff!='t-0'):
            if(self.bookvol_date_str_buff==datetime.strftime(datetime.now(),"%Y-%m-%d")):
                self.bookvol_date_str_buff = 't-0'
            else:
                if(self.date_range_str_list==None):
                    list_logging_csv_date_se = pd.Series([datetime.strptime(i.replace(".csv",""),"%Y%m%d") for i in os.listdir(f"./logging_csv/{self.symbol}.bk")])
                    hist_csv_date_se = pd.to_datetime(self.symbol_hist_df['Date'])
                    date_range_se = pd.concat([list_logging_csv_date_se],ignore_index=True).sort_values()
                    self.date_range_str_list = date_range_se[date_range_se!=datetime(*datetime.now().date().timetuple()[:6])].dt.strftime("%Y-%m-%d").tolist()
                
                if(self.bookvol_date_str_buff == self.date_range_str_list[-1]):
                    self.bookvol_date_str_buff = 't-0'
                else:
                    self.bookvol_date_str_buff = self.date_range_str_list[self.date_range_str_list.index(self.bookvol_date_str_buff)+1]

            self.select_bookvol_dataframe_by_date(self.bookvol_date_str_buff) #draw txt if 'not found' or 'wait'
            self.select_candle_dataframe_by_date(self.bookvol_date_str_buff) #draw txt if 'not found' or 'wait'
            
            if(isinstance(self.bookvol_df_buff,pd.DataFrame)==True):
                self.normalize_bookvol_dataframe()
                self.plot_to_bookvol_axis()
                self.set_scale_bookvol_axis()

            if(isinstance(self.candle_se_buff,pd.Series)==True):
                self.set_scale_candle_axis()
                self.plot_to_candle_axis()

            self.fig.canvas.draw_idle() #draw plot data
        '''

    def press_key_prev(self):
        if(self.bookvol_date_str_buff=='t-0'):
            if(self.date_range_str_list==None):
                sorted_logging_csv_date_se = pd.Series([datetime.strptime(i.replace(".csv",""),"%Y%m%d") for i in os.listdir(f"./logging_csv/{self.symbol}.bk")]).sort_values()
                self.date_range_str_list = sorted_logging_csv_date_se[sorted_logging_csv_date_se!=datetime(*datetime.now().date().timetuple()[:6])].dt.strftime("%Y-%m-%d").tolist()

            self.bookvol_date_str_buff = self.date_range_str_list[-1]
        else:
            self.bookvol_date_str_buff = self.date_range_str_list[self.date_range_str_list.index(self.bookvol_date_str_buff)-1]
        
        self.select_bookvol_dataframe_by_date(self.bookvol_date_str_buff)
        self.select_candle_dataframe_by_date(self.bookvol_date_str_buff)

        if(isinstance(self.bookvol_df_buff,pd.DataFrame)==True):
                self.normalize_bookvol_dataframe()
                self.plot_to_bookvol_axis()
                self.set_scale_bookvol_axis()

        if(isinstance(self.candle_se_buff,pd.Series)==True):
            self.plot_to_candle_axis()
            self.set_scale_candle_axis()

        self.fig.canvas.draw_idle() #draw plot data

        '''
        if(isinstance(self.bookvol_df_buff,pd.DataFrame)==False):
            self.symbol_hist_df = pd.read_csv(f"./symbol_hist_csv/{self.symbol}.bk.csv",index_col=False)

        if(self.bookvol_date_str_buff!=self.symbol_hist_df['Date'].iloc[0]):
            if(self.bookvol_date_str_buff=='t-0'):
                if(self.date_range_str_list==None):
                    list_logging_csv_date_se = pd.Series([datetime.strptime(i.replace(".csv",""),"%Y%m%d") for i in os.listdir(f"./logging_csv/{self.symbol}.bk")])
                    hist_csv_date_se = pd.to_datetime(self.symbol_hist_df['Date'])
                    date_range_se = pd.concat([list_logging_csv_date_se],ignore_index=True).sort_values()
                    self.date_range_str_list = date_range_se[date_range_se!=datetime(*datetime.now().date().timetuple()[:6])].dt.strftime("%Y-%m-%d").tolist()
                    
                self.bookvol_date_str_buff = self.date_range_str_list[-1]
            else:
                self.bookvol_date_str_buff = self.date_range_str_list[self.date_range_str_list.index(self.bookvol_date_str_buff)-1]

            self.select_bookvol_dataframe_by_date(self.bookvol_date_str_buff) #draw txt if 'not found' or 'wait'
            self.select_candle_dataframe_by_date(self.bookvol_date_str_buff) #draw txt if 'not found' or 'wait'
           
            if(isinstance(self.bookvol_df_buff,pd.DataFrame)==True):
                self.normalize_bookvol_dataframe()
                self.plot_to_bookvol_axis()
                self.set_scale_bookvol_axis()

            if(isinstance(self.candle_se_buff,pd.Series)==True):
                self.plot_to_candle_axis()
                self.set_scale_candle_axis()

            self.fig.canvas.draw_idle() #draw plot data
        '''
    def press_key_jump_to_date(self):
        while True:
            try:
                user_date_input = self.ask_string(title=f'book_val_graph : {self.symbol}',prompt="ENTER DATE | format YYYYMMDD\t\t\t")
                
                if(user_date_input==None):
                    break
                elif(user_date_input=='' or user_date_input=='t-0'):
                    #jump to t-0 and plot
                    self.bookvol_date_str_buff = 't-0'
                    self.send_request_logging_df()
                    break
                else:
                    #jump to input date (if in range and exist)
                    user_date_input = datetime.strptime(user_date_input,"%Y%m%d")
                    list_logging_csv_symbol = os.listdir(f"./logging_csv/{self.symbol}.bk")
                    start_logging_csv_date = datetime.strptime(list_logging_csv_symbol[0].replace(".csv",""),"%Y%m%d")
                    end_logging_csv_date = datetime.strptime(list_logging_csv_symbol[-1].replace(".csv",""),"%Y%m%d")
                    
                    if(user_date_input>=start_logging_csv_date and user_date_input<=end_logging_csv_date):
                        #jump to date and plot
                        self.bookvol_date_str_buff = datetime.strftime(user_date_input,"%Y-%m-%d")
                        self.select_bookvol_dataframe_by_date(self.bookvol_date_str_buff) #draw txt if 'not found' or 'wait'
                        self.select_candle_dataframe_by_date(self.bookvol_date_str_buff) #draw txt if 'not found' or 'wait'
                        
                        if(isinstance(self.bookvol_df_buff,pd.DataFrame)==True):
                            self.normalize_bookvol_dataframe() #normalize and repair incomplate self.bookvol_df_buff
                            self.plot_to_bookvol_axis()
                            self.set_scale_bookvol_axis()
                        
                        if(isinstance(self.candle_se_buff,pd.Series)==True):
                            self.plot_to_candle_axis()
                            self.set_scale_candle_axis()

                        self.fig.canvas.draw_idle() #draw plot data
                        break
                    else:
                        ctypes.windll.user32.MessageBoxW(0,f'book_val_graph : {self.symbol}','date format error please insert date again',0)
            except:
                ctypes.windll.user32.MessageBoxW(0,f'book_val_graph : {self.symbol}','date format error please insert date again',0)
                continue

    #ask string dialog
    def ask_string(self,title='',prompt=''):
        threading.Thread(target=focus_window,args=(title,),daemon=True).start()
        return simpledialog.askstring(title=title,prompt=prompt,parent=rt)

    def press_key_set_min_vol(self):
        while True:
            try:
                user_minvol_input = self.ask_integer(title=f'book_val_graph : {self.symbol}',prompt="ENTER MINIMUM VOL. LIMIT | K.unit")
                #re-normalize current date
                if(user_minvol_input!=None and user_minvol_input>=100):
                    self.ax1.cla()
                    self.config_bookvol_description()
                    #reset value and re-plot
                    self.minlim_vol_filter = user_minvol_input
                    self.normalize_bookvol_dataframe() #normalize and repair incomplate self.bookvol_df_buff
                    self.plot_to_bookvol_axis()
                    self.set_scale_bookvol_axis()
                    self.fig.canvas.draw_idle() #draw plot data
                    break
                elif(user_minvol_input==None):
                    break
                else:
                    raise Exception("empty type_error or input limit < 100")
            except:
                ctypes.windll.user32.MessageBoxW(0,f'book_val_graph : {self.symbol}','empty minimum vol.limit or limit < 100 please insert k.unit again',0)
                continue
    
    def ask_integer(self,title='',prompt=''):
        threading.Thread(target=focus_window,args=(title,),daemon=True).start()
        return simpledialog.askinteger(title=title,prompt=prompt,parent=rt)
    
    #config cursor
    def config_crosshair_cursor(self): #(bliting type)
        self.cursor = cross_hair_cursor(self.ax1)
        #do not use cursor , use self.cursor instead because when mpl re-call cross_hair_cursor(self.ax1) class it's not found
        self.fig.canvas.mpl_connect('motion_notify_event',self.cursor.on_mouse_move)
    
    def config_handle_close_event(self):
        self.fig.canvas.mpl_connect('close_event',self.on_close)
    
    def on_close(self,event):
        print('on_close handler')
        self.thread_receiver_pipe.send([self.symbol,'close'])

    #config_axis_vol_graph
    def config_axis_bookvol(self):
        self.ax1 = self.fig.add_subplot(self.sgs1[:16,:12],facecolor=self.bgcolor)
        self.ax1.spines['top'].set_color(self.color)
        self.ax1.spines['left'].set_color(self.color)
        self.ax1.spines['right'].set_color(self.color)
        self.ax1.spines['bottom'].set_color(self.color)
        self.ax1.tick_params(axis='x', colors=self.color)
        self.ax1.tick_params(axis='y', colors=self.color)
        self.ax1.set_title(self.symbol,multialignment='center',fontsize=15,color=self.color)
        self.ax1.set_ylabel('price',fontsize=12,color=self.color)
        self.ax1.set_xlabel('time  ',multialignment='center',labelpad=5,fontsize=12,color=self.color)
        self.ax1.text(0.00,1.01, self.bookvol_date_str_buff,multialignment='left',transform=self.ax1.transAxes,color=self.color, fontsize=12)
        self.ax1.text(0.01,0.01, 'bid',multialignment='center',transform=self.ax1.transAxes,color=self.color, fontsize=12)
        self.ax1.text(0.01,0.96, 'offer',multialignment='center',transform=self.ax1.transAxes,color=self.color, fontsize=12)

    def config_bookvol_description(self):
        self.ax1.set_title(self.symbol,multialignment='center',fontsize=15,color=self.color)
        self.ax1.set_ylabel('price',fontsize=12,color=self.color)
        self.ax1.set_xlabel('time  ',multialignment='center',labelpad=5,fontsize=12,color=self.color)
        self.ax1.text(0.00,1.01, self.bookvol_date_str_buff,multialignment='left',transform=self.ax1.transAxes,color=self.color, fontsize=12)
        self.ax1.text(0.01,0.01, 'bid',multialignment='center',transform=self.ax1.transAxes,color=self.color, fontsize=12)
        self.ax1.text(0.01,0.96, 'offer',multialignment='center',transform=self.ax1.transAxes,color=self.color, fontsize=12)

    #config_axis_candle
    def config_axis_candle(self):
        self.bar_width = .3
        self.bar_width_shadow = .03
        self.ax2 = self.fig.add_subplot(self.sgs1[:,-3:],facecolor=self.bgcolor)
        self.ax2.spines['top'].set_color(self.color)
        self.ax2.spines['left'].set_color(self.color)
        self.ax2.spines['right'].set_color(self.color)
        self.ax2.spines['bottom'].set_color(self.color)
        self.ax2.tick_params(axis='x', colors=self.color)
        self.ax2.tick_params(axis='y', colors=self.color)
        #self.ax2.set_ylabel('price',multialignment='center',labelpad=3,fontsize=12,color=self.color)
        self.ax2.set_title('candle',fontsize=12,color=self.color)
    
    def config_candle_description(self):
        #self.ax2.set_ylabel('price',multialignment='center',labelpad=3,fontsize=12,color=self.color)
        self.ax2.set_title('candle',fontsize=12,color=self.color)

    #prepare dataframe to plot
    def select_bookvol_dataframe_by_date(self,date_str='t-0'):
        self.ax1.cla()
        self.config_bookvol_description()
        if(date_str=='t-0'):
            #prepare latest dataframe
            if(self.start_bookvol_datetime == None or self.start_bookvol_datetime.date()!=datetime.now().date()):
                self.start_bookvol_datetime = datetime.combine(datetime.now().date(),datetime.min.time()) + timedelta(hours=10)
            
            if(self.end_bookvol_datetime == None or self.end_bookvol_datetime.date()!=datetime.now().date()):
                self.end_bookvol_datetime = datetime.combine(datetime.now().date(),datetime.min.time()) + timedelta(hours=16,minutes=30)

            if(self.bookvol_df_buff == None or len(self.bookvol_df_buff)==0):
                #print(f"{self.symbol} : error {type(e)} : select_bookvol_dataframe_by_date")
                self.bookvol_df_buff = None
                self.waiting_plot_for_bookvol_graph()

        elif(date_str!='t-0'):
            #prepare hist dataframe
            try:
                #global_logging_dict_df==None
                if(len(os.listdir(f'./logging_csv/{self.symbol}.bk'))>0):
                    if(self.last_file_date_str==None):
                        self.last_file_date_str = [i.replace('.csv','') for i in os.listdir(f"./logging_csv/{self.symbol}.bk/")][-1]
                    else:
                        self.last_file_date_str = date_str.replace("-","")
                    self.start_bookvol_datetime = datetime.strptime(f"{self.last_file_date_str} 10:00","%Y%m%d %H:%M")
                    self.end_bookvol_datetime = datetime.strptime(f"{self.last_file_date_str} 16:30","%Y%m%d %H:%M")
                    self.bookvol_df_buff = pd.read_csv(f"./logging_csv/{self.symbol}.bk/{self.last_file_date_str}.csv",index_col=False)[['Date','bid1','offer1','Open','High','Low','Close']]

            except Exception as e:
                #print(f"{self.symbol} : error {type(e)} : select_bookvol_dataframe_by_date")
                #print(e)
                self.bookvol_df_buff = None
                self.empty_plot_for_bookvol_graph()

    def select_candle_dataframe_by_date(self,date_str='t-0'):
        self.ax2.cla()
        self.config_candle_description()
        if(date_str=='t-0' or date_str == None):
            if(self.candle_se_buff == None):
                self.waiting_plot_for_candle_graph()
        else:
            try:
                if(isinstance(self.bookvol_df_buff,pd.DataFrame)==False):
                    if(self.last_file_date_str==None):
                        self.last_file_date_str = [i.replace('.csv','') for i in os.listdir(f"./logging_csv/{self.symbol}.bk/")][-1]
                    else:
                        self.last_file_date_str = date_str.replace("-","")

                    self.candle_se_buff = pd.read_csv(f"./logging_csv/{self.symbol}.bk/{self.last_file_date_str}.csv",index_col=False)[['Date','Open','High','Low','Close']].iloc[-1]
                
                else:
                    self.candle_se_buff = self.bookvol_df_buff[['Date','Open','High','Low','Close']].iloc[-1]
                    
            except FileNotFoundError:
                self.candle_se_buff = None
                self.empty_plot_for_candle_graph()
            
            except IndexError:
                self.candle_se_buff = None
                self.empty_plot_for_candle_graph()

    #prepare dataframe to plot
    def normalize_bookvol_dataframe(self):
        if(self.bookvol_df_buff['Date'].dtypes.name=='object'):
            self.bookvol_df_buff['Date'] = pd.to_datetime(self.bookvol_df_buff['Date'])
        
        self.bookvol_df_buff = self.bookvol_df_buff.loc[(self.bookvol_df_buff['Date']>=self.start_bookvol_datetime) & (self.bookvol_df_buff['Date']<=self.end_bookvol_datetime),['Date','bid1','offer1']].copy()
        self.bookvol_df_buff = self.bookvol_df_buff.loc[self.bookvol_df_buff['bid1'].apply(lambda x:(x != None) and ('ATC' not in x)),:].reset_index(drop=True).copy()
       
        for i,r in self.bookvol_df_buff.iterrows():
            self.bookvol_df_buff.loc[i,'bid_price'],self.bookvol_df_buff.loc[i,'bid_vol']= r['bid1'].strip().split("|")
            self.bookvol_df_buff.loc[i,'offer_price'],self.bookvol_df_buff.loc[i,'offer_vol'] = r['offer1'].strip().split("|")

        self.bookvol_df_buff = self.bookvol_df_buff.astype({'bid_vol':'float64','bid_price':'float64','offer_vol':'float64','offer_price':'float64'})
        self.bookvol_df_buff['bid_chg'] = self.bookvol_df_buff['bid_vol'].diff().apply(lambda x:x if(x>self.minlim_vol_filter or x<-self.minlim_vol_filter) else 0)
        self.bookvol_df_buff.loc[(self.bookvol_df_buff['bid_price'].diff()!=0) ,'bid_chg'] = 0
        self.bookvol_df_buff['offer_chg'] = self.bookvol_df_buff['offer_vol'].diff().apply(lambda x:x if(x>self.minlim_vol_filter or x<-self.minlim_vol_filter) else 0)
        self.bookvol_df_buff.loc[(self.bookvol_df_buff['offer_price'].diff()!=0) ,'offer_chg'] = 0

        self.check_fill_empty_to_bookvol_plot()

        #seting scale to book_vol axis before plot
    def set_scale_bookvol_axis(self):
        self.ax_minlim = (self.bookvol_df_buff['bid_price'] - self.bookvol_df_buff['bid_chg_pos'].abs()).min()
        minlim_price_range = price_range(self.ax_minlim)
        self.ax_maxlim = (self.bookvol_df_buff['offer_price'] + self.bookvol_df_buff['offer_chg_pos'].abs()).max()
        self.ax1.set_ylim(self.ax_minlim-(minlim_price_range*0.5),self.ax_maxlim+(minlim_price_range*0.5)) #compensate minlim and maxlim (margin 1/5 of price spread)
        self.ax1.set_xlim(-(276*0.2),276+276*0.2)

        #plot axis_vol_graph
    def plot_to_bookvol_axis(self):
        max_volume_chg = self.bookvol_df_buff[['bid_chg','offer_chg']].abs().max().max()
        diff_max_min_price = (self.bookvol_df_buff['offer_price'].max()-self.bookvol_df_buff['offer_price'].min())
        self.bookvol_df_buff['bid_chg_pos'] = (self.bookvol_df_buff['bid_chg']/max_volume_chg)*diff_max_min_price #remain negative state (incase value is negative)
        self.bookvol_df_buff['offer_chg_pos'] = (self.bookvol_df_buff['offer_chg']/max_volume_chg)*diff_max_min_price #remain negative state (incase value is negative)
        max_price_range = price_range(self.bookvol_df_buff['offer_price'].max())

        bookvol_df_buff_filter_except_nan = self.bookvol_df_buff.loc[~self.bookvol_df_buff['bid1'].isna()]

        self.ax1.errorbar(bookvol_df_buff_filter_except_nan.index,bookvol_df_buff_filter_except_nan['offer_price'],[[0]*len(bookvol_df_buff_filter_except_nan),bookvol_df_buff_filter_except_nan['offer_chg_pos'].abs()],fmt='o',markersize=0,ecolor=bookvol_df_buff_filter_except_nan['offer_chg'].apply(lambda x:self.downcolor if(x>=0) else self.upcolor))
        for c in bookvol_df_buff_filter_except_nan['offer_chg_pos'].index:
            offer_chg_pos_buff = bookvol_df_buff_filter_except_nan.loc[c,'offer_chg_pos']
            if(offer_chg_pos_buff!=0):
                self.ax1.text(x=c,y=(bookvol_df_buff_filter_except_nan.loc[c,'offer_price']+abs(offer_chg_pos_buff)+max_price_range*0.1),s=f"[{round(c/60,1)}]"+str(bookvol_df_buff_filter_except_nan.loc[c,'offer_chg'].round(1))+'K',horizontalalignment='center',fontsize=12,color=self.downcolor if(offer_chg_pos_buff>=0) else self.upcolor)

        self.ax1.plot(bookvol_df_buff_filter_except_nan.index,bookvol_df_buff_filter_except_nan['offer_price'],color=self.color)

        self.ax1.errorbar(bookvol_df_buff_filter_except_nan.index,bookvol_df_buff_filter_except_nan['bid_price'],[bookvol_df_buff_filter_except_nan['bid_chg_pos'].abs(),[0]*len(bookvol_df_buff_filter_except_nan)],fmt='o',markersize=0,ecolor=bookvol_df_buff_filter_except_nan['bid_chg'].apply(lambda x:self.upcolor if(x>=0) else self.downcolor))
        for c in bookvol_df_buff_filter_except_nan['bid_chg_pos'].index:
            bid_chg_pos_buff = bookvol_df_buff_filter_except_nan.loc[c,'bid_chg_pos']
            if(bid_chg_pos_buff!=0):
                self.ax1.text(x=c,y=(bookvol_df_buff_filter_except_nan.loc[c,'bid_price']-abs(bid_chg_pos_buff)-max_price_range*0.2),s=f"[{round(c/60,1)}]"+str(bookvol_df_buff_filter_except_nan.loc[c,'bid_chg'].round(1))+'K',horizontalalignment='center',fontsize=12,color=(self.upcolor if(bid_chg_pos_buff>=0) else self.downcolor))

        self.ax1.plot(bookvol_df_buff_filter_except_nan.index,bookvol_df_buff_filter_except_nan['bid_price'],color=self.color)
    
    def check_fill_empty_to_bookvol_plot(self):
        #len(self.bookvol_df_buff)<276 for hist if bookvol_df_buff
        if((self.bookvol_date_str_buff=='t-0') or (self.bookvol_date_str_buff!='t-0' and len(self.bookvol_df_buff)<276)):
            problem_date_str = self.bookvol_df_buff['Date'].iloc[0].strftime("%Y-%m-%d")
            datetime_prototype_df = pd.DataFrame({'Date':pd.to_datetime(problem_date_str+' '+self.time_prototype_df['Date'])})
            problem_datetime_rounded_se = pd.to_datetime(self.bookvol_df_buff['Date']).dt.round('min')
            filer_df = pd.DataFrame({'Date':datetime_prototype_df[~datetime_prototype_df['Date'].isin(problem_datetime_rounded_se)]['Date']})
            self.bookvol_df_buff['Date'] = pd.to_datetime(self.bookvol_df_buff['Date'])
            filed_df = pd.concat([filer_df,self.bookvol_df_buff]).sort_values(by='Date').reset_index(drop=True)
            self.bookvol_df_buff = filed_df[filed_df['Date']<=self.bookvol_df_buff['Date'].iloc[-1]].copy()
            self.bookvol_df_buff['bid1'] = self.bookvol_df_buff['bid1'].astype("object")
            self.bookvol_df_buff.loc[self.bookvol_df_buff['bid1'].isna(),'bid1'] = None
            self.bookvol_df_buff['offer1'] = self.bookvol_df_buff['offer1'].astype("object")
            self.bookvol_df_buff.loc[self.bookvol_df_buff['offer1'].isna(),'offer1'] = None
        
        #plot waiting txt for vol_graph (incase latest data not coming yet)
    def waiting_plot_for_bookvol_graph(self):
        self.bookvol_axis_status = self.ax1.text(0.5,0.5,'waiting',ha='center', va='center',color=self.color, fontsize=12)

        #plot empty txt for vol_graph (incase data error or not found)
    def empty_plot_for_bookvol_graph(self):
        self.bookvol_axis_status = self.ax1.text(0.5,0.5,'not found',ha='center', va='center',color=self.downcolor, fontsize=12)

        #seting scale to candle axis before plot
    def set_scale_candle_axis(self):
        minlim_price_range = price_range(self.candle_se_buff['Low'])
        self.ax2.set_ylim(self.candle_se_buff['Low']-(minlim_price_range*0.5),self.candle_se_buff['High']+(minlim_price_range*0.5))

        #plot axis_candle_graph
    def plot_to_candle_axis(self):
        #candle
        if(self.candle_se_buff['Close']>self.candle_se_buff['Open']):
            self.ax2.bar(0, self.candle_se_buff['Close']-self.candle_se_buff['Open'], self.bar_width, edgecolor=self.upcolor , bottom=self.candle_se_buff['Open'], color=self.upcolor)
            self.ax2.bar(0, self.candle_se_buff['High']-self.candle_se_buff['Close'], self.bar_width_shadow, edgecolor=self.upcolor , bottom=self.candle_se_buff['Close'], color=self.upcolor)
            self.ax2.bar(0, self.candle_se_buff['Low'].min()-self.candle_se_buff['Open'], self.bar_width_shadow, edgecolor=self.upcolor , bottom=self.candle_se_buff['Open'], color=self.upcolor)
        else:
            self.ax2.bar(0, self.candle_se_buff['Close']-self.candle_se_buff['Open'], self.bar_width, edgecolor=self.downcolor , bottom=self.candle_se_buff['Open'], color=self.downcolor)
            self.ax2.bar(0, self.candle_se_buff['High']-self.candle_se_buff['Open'], self.bar_width_shadow, edgecolor=self.downcolor , bottom=self.candle_se_buff['Open'], color=self.downcolor)
            self.ax2.bar(0, self.candle_se_buff['Low'].min()-self.candle_se_buff['Close'], self.bar_width_shadow, edgecolor=self.downcolor , bottom=self.candle_se_buff['Close'], color=self.downcolor)

    def waiting_plot_for_candle_graph(self):
        self.candle_axis_status = self.ax2.text(0.5,0.5,'waiting', ha='center', va='center', color=self.color, fontsize=12)

        #plot empty for candle_graph (incase data error or not found)
    def empty_plot_for_candle_graph(self):
        self.candle_axis_status = self.ax2.text(0.5,0.5,'not found', ha='center', va='center', color=self.downcolor, fontsize=12)

    #for alternative process
    def _process_assign_task_and_alive_on_show(self):
        #release graph timer thread to auto_flushing and listening data comming
        #print('processing running')
        self.config_handle_close_event()
        #self.config_crosshair_cursor()
        self.config_binding_keyboard()
        timer = self.fig.canvas.new_timer(interval=500)
        timer.add_callback(self.__thread_auto_flush_and_listener)
        timer.start()
        plt.tight_layout()
        plt.show() #process alive on this

    #for thread of alternative process
    def __thread_auto_flush_and_listener(self):
        while self.thread_receiver_pipe.poll():
            logging_df_buff = self.thread_receiver_pipe.recv()
            if(self.bookvol_date_str_buff=='t-0'):
                #incase graph running at latest date
                #plot for bookvol
                self.bookvol_df_buff = logging_df_buff[['Date','bid1','offer1']]
                self.candle_se_buff = logging_df_buff.iloc[-1][['Open','High','Low','Close']]
                self.select_bookvol_dataframe_by_date(self.bookvol_date_str_buff) #draw txt if 'not found' or 'wait'
                self.select_candle_dataframe_by_date(self.bookvol_date_str_buff)
                if(isinstance(self.bookvol_df_buff,pd.DataFrame)==True and isinstance(self.candle_se_buff,pd.Series)==True):
                    self.normalize_bookvol_dataframe() #normalize and repair incomplate self.bookvol_df_buff
                    self.plot_to_bookvol_axis()
                    self.set_scale_bookvol_axis()
                    #self.plot_to_candle_axis()
                    #self.set_scale_candle_axis()
                    self.fig.canvas.draw_idle()

    #internal for request logging_df to plot bookvol
    def send_request_logging_df(self):
        self.thread_receiver_pipe.send([self.symbol,'request_logging_df'])
            
    #external for main process and main thread (for update plot data)
    def send_plot(self,logging_df):
        self.sender_pipe.send(logging_df)

    #external for main process and sub-thread (for unregist bookvol graph obj)
    def thread_send_receiver_listener(self):
        print('threading start')
        global global_logging_dict_df
        while True:
            obj_data_list = self.sender_pipe.recv()
            print('threading receive')
            print(obj_data_list)
            if(obj_data_list[0]==self.symbol and obj_data_list[1]=='close'):
                print(f'deleting {self.symbol}')
                del global_logging_dict_df[self.symbol]
                print(global_logging_dict_df)
                break
            elif(obj_data_list[0]==self.symbol and obj_data_list[1]=='request_logging_df'):
                print('response logging df')
                try:
                    if(len(global_logging_dict_df[self.symbol])>0):
                        self.sender_pipe.send(global_logging_dict_df[self.symbol])
                except:
                    #incase global_logging_dict_df[self.symbol] key error
                    pass

def regist_bookvol_graph(symbol):
    global global_logging_dict_df
    #check bookvol graph not duplicates
    if(symbol not in global_logging_dict_df.keys()):
        global_logging_dict_df[symbol] = bookvol_graph(symbol) 
        threading.Thread(target=global_logging_dict_df[symbol].thread_send_receiver_listener,daemon=True).start()
        print(f'regist {symbol} complete')

if __name__=='__main__':
    print('testing calling graph')
    global_logging_dict_df = {} #global

    #call state
    regist_bookvol_graph('bam') #regist and open bookvol graph by symbol 

    #send state
    try:
        #global_logging_dict_df['some_symbol'].send_plot() #test send invaild symbol
        #global_logging_dict_df['bam'].send_plot() #test send vaild symbol
        pass
    except KeyError:
        print('except')
        pass

    #report total
    #print(global_logging_dict_df)

    # test delete symbol
    #del global_logging_dict_df['bam']

    #report after delete
    #print(global_logging_dict_df)
    print('current global_logging_dict_df')
    print(global_logging_dict_df)
    time.sleep(10)
    print('after close global_logging_dict_df')
    print(global_logging_dict_df)