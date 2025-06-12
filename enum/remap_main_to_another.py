from enum import Enum

'''
เมื่อเรามีหลาย exchange ที่กำหนดรูปแบบ symbol ไม่เหมือนกัน 
แต่จริงๆคือ symbol ตัวเดียวกัน เช่น BTC_USDT ก็คือ BTCUSDT , BTC-USDT , BTC/USDT
เราสามารถสร้าง enum กำหนด symbol มาตรฐาน และค่อยแปลง symbol นั้นไปตาม exchange นั้นๆอีกที 
'''

class main_symbol_Exchange(Enum):
    BTC_USDT = "BTC_USDT"

#----------destination exchange lib-------------
class symbol_ExchangeA(Enum):
    BTC_USDT = "BTC/USDT"
    ETH_USDT = "ETH/USDT"
    # สามารถเพิ่มเหรียญอื่นๆ ได้ตามต้องการ

def convert_symbol(symbol_name:str,to_exchange_class):
    try:
        # ใช้ getattr() เพื่อดึงค่า enum จากชื่อ symbol ในรูปแบบ string
        if(symbol_name not in [i for i in symbol_ExchangeA.__members__]):
            raise AttributeError
        symbol = getattr(to_exchange_class, symbol_name)
        return symbol.value
    except AttributeError:
        return None  # คืน None ถ้าไม่เจอ symbol

#----------------------------------------------

if __name__=='__main__':
    '''
    ต้นทาง (main) passing_symbol='BTC_USDT' ไป function หรือ class ปลายทาง
    ปลานทาง (ExchangeA) : convert_symbol(passing_symbol,symbol_ExchangeA) 
    '''
    print(convert_symbol('BTC_USDT',symbol_ExchangeA))
    import pdb;pdb.set_trace()