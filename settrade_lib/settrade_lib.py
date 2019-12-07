from tools_lib.scrap_tools import *

#set url
settrade_data_url = "https://www.settrade.com/brokerpage/IPO/StaticPage/Home/ticker.html"

def settrade_build_source():
    source = None
    try : 
        source = build_soup(settrade_data_url)
    except Exception as error:
        raise Exception(error)
    return source 

#get last set value
def get_last_set(source):
    return source.select("b:nth-of-type(2)")[0].get_text().split() 

def get_last_set50(source):
    return source.select("b:nth-of-type(3)")[0].get_text().split()
#get last set50 value
#get last stock_name price