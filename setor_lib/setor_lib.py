from tools_lib.scrap_tools import *

setor_data_url = "https://marketdata.set.or.th/mkt/investortype.do"

def setor_build_source():
    source = None
    try : 
        source = build_soup(setor_data_url)
    except Exception as error:
        raise Exception(error)
    return source

#get last set value
#float(source.find_all("table",class_="table table-info")[0] <--[0] it's mean today
def get_trading_group_d(source):
    trading_group_set = {
        'bvd':None,'svd':None,'d':None
    }

    trading_group_set['bvd'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(1) > td")[1].get_text().replace(",","").strip())
    trading_group_set['svd'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(1) > td")[3].get_text().replace(",","").strip())
    trading_group_set['d'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(1) > td")[5].get_text().replace(",","").strip())

    return trading_group_set

def get_trading_group_s(source):
    trading_group_set = {
        'bvs':None,'svs':None,'s':None
    }

    trading_group_set['bvs'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(2) > td")[1].get_text().replace(",","").strip())
    trading_group_set['svs'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(2) > td")[3].get_text().replace(",","").strip())
    trading_group_set['s'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(2) > td")[5].get_text().replace(",","").strip())

    return trading_group_set

def get_trading_group_f(source):
    trading_group_set = {
        'bvf':None,'svf':None,'f':None
    }

    trading_group_set['bvf'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(3) > td")[1].get_text().replace(",","").strip())
    trading_group_set['svf'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(3) > td")[3].get_text().replace(",","").strip())
    trading_group_set['f'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(3) > td")[5].get_text().replace(",","").strip())

    return trading_group_set

def get_trading_group_g(source):
    trading_group_set = {
        'bvg':None,'svg':None,'g':None
    }

    trading_group_set['bvg'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(4) > td")[1].get_text().replace(",","").strip())
    trading_group_set['svg'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(4) > td")[3].get_text().replace(",","").strip())
    trading_group_set['g'] = float(source.find_all("table",class_="table table-info")[0].select("tbody > tr:nth-of-type(4) > td")[5].get_text().replace(",","").strip())

    return trading_group_set