from tools_lib.scrap_tools import *
import pdb

set_data_url = "https://marketdata.set.or.th/mkt/investortype.do"

try : 
    source = build_soup(set_data_url)
except Exception as error:
    raise Exception(error) 

#get last set value
#float(source.find_all("table",class_="table table-info")[0] <--[0] it's mean today
def get_trading_group_d():
    global source
    trading_group_set = {
        'pv':None,'sv':None,'v':None
    }

    trading_group_set['pv'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(1) > td")[1].get_text().replace(",","").strip())
    trading_group_set['sv'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(1) > td")[3].get_text().replace(",","").strip())
    trading_group_set['v'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(1) > td")[5].get_text().replace(",","").strip())

    return trading_group_set

def get_trading_group_s():
    global source
    trading_group_set = {
        'pv':None,'sv':None,'v':None
    }

    trading_group_set['pv'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(2) > td")[1].get_text().replace(",","").strip())
    trading_group_set['sv'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(2) > td")[3].get_text().replace(",","").strip())
    trading_group_set['v'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(2) > td")[5].get_text().replace(",","").strip())

    return trading_group_set

def get_trading_group_f():
    global source
    trading_group_set = {
        'pv':None,'sv':None,'v':None
    }

    trading_group_set['pv'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(3) > td")[1].get_text().replace(",","").strip())
    trading_group_set['sv'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(3) > td")[3].get_text().replace(",","").strip())
    trading_group_set['v'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(3) > td")[5].get_text().replace(",","").strip())

    return trading_group_set

def get_trading_group_g():
    global source
    trading_group_set = {
        'pv':None,'sv':None,'v':None
    }

    trading_group_set['pv'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(4) > td")[1].get_text().replace(",","").strip())
    trading_group_set['sv'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(4) > td")[3].get_text().replace(",","").strip())
    trading_group_set['v'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(4) > td")[5].get_text().replace(",","").strip())

    return trading_group_set

if __name__ == "__main__":
    print(get_trading_group_d())
    print(get_trading_group_f())
    print(get_trading_group_g())
    print(get_trading_group_s())