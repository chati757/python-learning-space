from settrade.openapi import Investor
from profile import *

investor = Investor(
                app_id=profile_app_id,                                 # Your app ID
                app_secret=profile_app_secret, # Your app Secret
                broker_id=profile_broker_id,                                           
                app_code=profile_app_code,
                is_auto_queue=profile_is_auto_queue)

equity = investor.Equity(account_no=profile_account_no)

account_info = equity.get_account_info()

if(account_info['success']==True):
    print(f"limit : {account_info['data']['initial_credit_limit']}")
    print(f"initial_available : {account_info['data']['initial_line_available']}")
    print(f"line_available : {account_info['data']['line_available']}")
    