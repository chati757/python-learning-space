import configparser
from settrade_v2 import Investor
from settrade_v2 import errors
import threading
import time

'''
1. message สำหรับ on_messsage ต้องครอบด้วย threading.Lock ทุกครั้ง
2. build realtime ทั้งหมดทุก symbol ที่ต้องการเชื่อมต่อภายในครั้งเดียว (ใช้ loop list เข้ามาช่วย)
3. start subscriber ทั้งหมดทุก symbol ภายในครั่ง ไม่สั่งหลายครั้ง ไม่สั่งซ้ำซ้อน (ใช้ loop list เข้ามาช่วย)
4. end subscriber ทั้งหมดทุก symbol ภายในครั้งเดียว ไม่สั่ง stop บางส่วน (ใช้ loop list เข้ามาช่วย)
5. ทุกครั้งที่กลับมา connect ใหม่ตั้งสั่ง api_investor_login.RealtimeDataConnection() ใหม่
'''

if __name__=='__main__':
    config_api = configparser.RawConfigParser()
    config_api.read('./tools_lib/settrade_api.cfg')
    api_investor_login = Investor(    
        app_id=config_api.get('login','app_id'),    
        app_secret=config_api.get('login','secret'),
        broker_id=config_api.get('login','broker_id'),
        app_code="ALGO_EQ",
        is_auto_queue = True
    )

    api_realtime = api_investor_login.RealtimeDataConnection()
   
    lock = threading.Lock()
    def message(result):
        with lock:
            print('\n')
            print(threading.enumerate())
            print(result)

    symbol_list = ['PTT','AOT']

    # for build build all subscribe
    sub_list = []
    for s in symbol_list:
        sub_buff = api_realtime.subscribe_price_info(s.upper(),on_message=message)
        sub_list.append(sub_buff)

    time.sleep(3)
    # for start all subscribe
    for s in sub_list:
        s.start()

    import pdb;pdb.set_trace()
    # for stop all subscribe
    for s in sub_list:
        s.stop()