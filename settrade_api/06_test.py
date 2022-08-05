from settrade.openapi import Investor
from profile import *

investor = Investor(
                app_id=profile_app_id,# Your app ID
                app_secret=profile_app_secret,# Your app Secret
                broker_id=profile_broker_id,                                           
                app_code=profile_app_code,
                is_auto_queue=profile_is_auto_queue)

equity = investor.Equity(account_no="xerus-E")

#-----------------------------get account info----------------------------

account_info = equity.get_account_info()
if(account_info['success']==True):
    print(f"limit : {account_info['data']['initial_credit_limit']}")
    print(f"initial_available : {account_info['data']['initial_line_available']}")
    print(f"line_available : {account_info['data']['line_available']}")

#----------------------------get realtime symbol data---------------------
realtime = investor.RealtimeDataConnection()
# Callback function for subscribing AOT's bid offer
def on_message(result, subscriber):
    print(result)

# This is subscriber object
subscriber = realtime.subscribe_bid_offer("BANPU",on_message).start()

#----------------------------place order----------------------------------
place_order = equity.place_order(
    symbol="BANPU",
    price=16.8,
    volume=300,
    side="BUY",
    pin="000000"
    )

print(place_order)

#----------------------------list order-----------------------------------
order_list = equity.get_orders()

if(order_list['success']==True):
    for data in order_list['data']:
        print(f"datetime : {data['entry_time']}")
        print(f"order no : {data['order_no']}")
        print(f"symbol : {data['symbol']}")
        print(f"price : {data['price']}")
        print(f"vol : {data['vol']}")
        print(f"balance : {data['balance']}")
        print(f"status : {data['show_order_status']}")
        print('---------------------------')

#----------------------------cancel order---------------------------------
cancel_order = equity.cancel_order(order_no="<Ex.2735W8YPKP>", pin="000000")
print(cencel_order)