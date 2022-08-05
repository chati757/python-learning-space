from settrade.openapi import Investor
from profile import *

investor = Investor(
                app_id=profile_app_id,                                 # Your app ID
                app_secret=profile_app_secret, # Your app Secret
                broker_id=profile_broker_id,                                           
                app_code=profile_app_code,
                is_auto_queue = profile_is_auto_queue)

equity = investor.Equity(account_no=profile_account_no)

place_order = equity.place_order(
    symbol="BANPU",
    price=13.3,
    volume=300,
    side="BUY",
    pin="000000"
    )

print(place_order)