from settrade.openapi import Investor
from profile import *

investor = Investor(
                app_id=profile_app_id,                                 # Your app ID
                app_secret=profile_app_secret, # Your app Secret
                broker_id=profile_broker_id,                                           
                app_code=profile_app_code,
                is_auto_queue = profile_is_auto_queue)

equity = investor.Equity(account_no=profile_account_no)

res = equity.get_orders()

if(res['success']==True):
    for data in res['data']:
        print(f"datetime : {data['entry_time']}")
        print(f"order no : {data['order_no']}")
        print(f"symbol : {data['symbol']}")
        print(f"price : {data['price']}")
        print(f"vol : {data['vol']}")
        print(f"balance : {data['balance']}")
        print(f"status : {data['show_order_status']}")
        print('---------------------------')

import pdb;pdb.set_trace()