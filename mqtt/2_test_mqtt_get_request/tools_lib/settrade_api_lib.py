import time
from datetime import datetime
import pandas as pd
from settrade_v2 import Investor
from settrade_v2 import errors
import configparser
import requests

class settrade_api:
    def __init__(self,custom_config_path:str=None):
        self.try_count_connection_init = 5
        self.try_count_connection = self.try_count_connection_init
        self.config_api = configparser.RawConfigParser()
        if(custom_config_path==None):
            self.config_api.read('./tools_lib/settrade_api.cfg')
        else:
            self.config_api.read(custom_config_path)
        self.api_info_df = None
        self.api_investor_login = None
        self.api_equity = None
        self.api_market_data = None
        self.api_realtime_data = None

    #decorator
    def __if_err_try_to_reconnect(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            #except requests.exceptions.RequestException as e:
            #except settrade_v2.errors.SettradeError as e:
            except Exception as e: 
                if(e.__dict__!={}): # ใน settrade_v2.errors.SettradeError ; e ไม่ได้มีแค่ message มี status_code กับ code ด้วย (กรณีแรกแต่ e แสดงแค่ message)
                    print(e.__dict__) # Ex. {'code': 1, 'status_code': 2} ; เกิดจาก raise settrade_v2.errors.SettradeError(code=1,message='some_msg',status_code=2)
                print('try to reconnect credencial..')
                args[0].connect_credencial()  # เรียกใช้ resolve_problem() ของอ็อบเจกต์ self ที่ส่งผ่านเป็นอาร์กิวเมนต์
        return wrapper

    def connect_credencial(self):
        while True:
            try:
                #login state
                self.api_investor_login = Investor(    
                    app_id=self.config_api.get('login','app_id'),    
                    app_secret=self.config_api.get('login','secret'),
                    broker_id=self.config_api.get('login','broker_id'),
                    app_code="ALGO_EQ",
                    is_auto_queue = True
                )

                #build equity
                self.api_equity = self.api_investor_login.Equity(account_no=self.config_api.get('login','account_no'))
                #build market_data
                self.api_market_data = self.api_investor_login.MarketData()
                #build realtime_data
                self.api_realtime_data = self.api_investor_login.RealtimeDataConnection()

                self.try_count_connection = self.try_count_connection_init
                break

            except Exception as e:
                self.try_count_connection-=1
                if(self.try_count_connection<=0):
                    print(e)
                    raise Exception('connect_credencial : failed')
                
                print('connect_credencial : failed : waiting today after 09:31:00')
                while(datetime.now()<=datetime.now().replace(hour=9,minute=31,second=0,microsecond=0)):
                    time.sleep(1)
                print('connect_credencial : failed : trying..')
                continue

    @__if_err_try_to_reconnect
    def get_hist_df_by_symbol(self,symbol:str,limit:int,timeframe:str):
        market_data_by_symbol_buff = self.api_market_data.get_candlestick(symbol=symbol.upper(),limit=limit,interval=timeframe)
        buff_df = pd.DataFrame({
            'Date':market_data_by_symbol_buff['time'],
            'Open':market_data_by_symbol_buff['open'],
            'High':market_data_by_symbol_buff['high'],
            'Low':market_data_by_symbol_buff['low'],
            'Close':market_data_by_symbol_buff['close'],
            'Volume':market_data_by_symbol_buff['volume'],
            'Value':market_data_by_symbol_buff['value']
            })

        buff_df['Date'] = (pd.to_datetime(buff_df['Date'],unit='s') + pd.Timedelta(days=1)).dt.strftime('%Y-%m-%d')

        return buff_df

    @__if_err_try_to_reconnect
    def get_last_candlestick(self,symbol:str):
        data_buff = self.api_market_data.get_candlestick(symbol=symbol.upper(),limit=1,interval='1d')
        return {'Date':datetime.fromtimestamp(data_buff['time'][0]).strftime("%Y-%m-%d"),'Open':data_buff['open'][0],'High':data_buff['high'][0],'Low':data_buff['low'][0],'Close':data_buff['close'][0],'Volume':data_buff['volume'][0],'Value':data_buff['value'][0]}

    @__if_err_try_to_reconnect
    def get_quote_by_symbol(self,symbol:str):
        return self.api_market_data.get_quote_symbol(symbol.upper())
