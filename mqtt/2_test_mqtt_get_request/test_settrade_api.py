from tools_lib.settrade_api_lib import *
import pandas as pd

if __name__=='__main__':
    stapi = settrade_api()
    stapi.connect_credencial()
    
    df = stapi.get_hist_df_by_symbol('ptt',600,'1d')
    print(df)
    import pdb;pdb.set_trace()
    