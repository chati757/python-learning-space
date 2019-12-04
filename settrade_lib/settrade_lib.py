from tools_lib.scrap_tools import *

#set url
set_data_url = "https://www.settrade.com/brokerpage/IPO/StaticPage/Home/ticker.html"

try : 
    source = build_soup(set_data_url)
except Exception as error:
    raise Exception(error) 

#get last set value
def get_last_set():
    global source
    return source.select("b:nth-of-type(2)")[0].get_text().split() 

def get_last_set50():
    global source
    return source.select("b:nth-of-type(3)")[0].get_text().split()
#get last set50 value
#get last stock_name price