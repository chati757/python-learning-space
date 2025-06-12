from datetime import datetime
import threading
import time
import os
import json
import pandas as pd
from mqtt_lib.mqtt_local_lib import *

if __name__=='__main__':
    print(f'main PID  : {os.getpid()}')

    mqttlb = mqtt_local_broker(
        broker_config_file_path='./mqtt_lib/mosquitto.conf',
        persistence_db_file_path='./mqtt_lib/persistence_data/mosquitto.db',
        persistence_backup_dir='./mqtt_lib/persistence_data/',
        debug_mode=True
    )
    mqttlb.start()

    def mqttlc_on_message(client,userdata,msg):
        print('---------------------')
        print(f"Topic: {msg.topic}")
        print(f"Payload: {msg.payload.decode('utf-8')}")
        print(f"QoS: {msg.qos}")
        print(f"Retain flag: {msg.retain}")
        data = json.loads(msg.payload.decode('utf-8'))
        try:
            if(data['type']=='inmkt_canrec_candle_1d_df'):
                df = pd.read_csv(f'./symbol_hist_csv/{data["symbol"]}.bk.csv',index_col=False)
                #client.publish(f'project/get_response/{data["client_id"]}',df.to_json(orient='records'),qos=1,retain=False)
                mqttlc.publish_topic(f'get_response/{data["client_id"]}',df.to_json(orient='records'))
            else:
                raise Exception('unkown type message')
        except Exception as e:
            print(f'mqttlc_on_message : error : {e}')

    mqttlc = mqtt_local_client(
        config_userpass_file_path="./mqtt_lib/client_userpass.ini",
        username='testuser',
        topic='project/',
        mode='both',
        on_message_func=mqttlc_on_message
    )
    mqttlc.start()
    mqttlc.subscribe_topic('get_request')

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            mqttlb.stop_and_join()
            mqttlc.stop_and_join()
            break