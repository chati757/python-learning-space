from settrade.openapi import Investor
from profile import *

investor = Investor(
                app_id=profile_app_id,# Your app ID
                app_secret=profile_app_secret,# Your app Secret
                broker_id=profile_broker_id,                                           
                app_code=profile_app_code,
                is_auto_queue = profile_is_auto_queue)

realtime = investor.RealtimeDataConnection()

# Callback function for subscribing AOT's bid offer
def on_message(result, subscriber):
    print(result)

# This is subscriber object
subscriber = realtime.subscribe_bid_offer("BANPU",on_message).start()
