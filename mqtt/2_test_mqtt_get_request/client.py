from datetime import datetime
import threading
import time
import os
import json
import pandas as pd
from mqtt_lib.mqtt_local_lib import *

if __name__=='__main__':
    print(f'main PID  : {os.getpid()}')

    def mqttlc_on_message(client,userdata,msg):
        print('---------------------')
        print(f"Topic : {msg.topic}")
        print(f"Payload : {msg.payload.decode('utf-8')}")
        print(f"QoS : {msg.qos}")
        print(f"Retain flag : {msg.retain}")

        if('get_response/' in msg.topic):
            mqttlc.get_response_queue.put(msg.payload.decode('utf-8'))

    mqttlc = mqtt_local_client(
        config_userpass_file_path="./mqtt_lib/client_userpass.ini",
        username='testuser',
        topic='project/',
        mode='both',
        on_message_func=mqttlc_on_message
    )
    mqttlc.start()
    mqttlc.subscribe_topic(f'get_response/{mqttlc.client_id}')
    
    time.sleep(5)
    '''
    #ตัวอย่างการทำ Publish ทั่วไปเพื่อรอข้อความตอบกลับมาใน get_response/<client_id> topic
    mqttlc.publish_topic('get_request',json.dumps({
        'client_id':mqttlc.client_id,
        'symbol':'ptt',
        'type':'inmkt_canrec_candle_1d_df',
        }))
    '''

    #ตัวอย่างการทำ publish แบบ get_request รอข้อความ return มาที่เดียวกัน
    data = mqttlc.mqtt_get_request({
        'client_id':mqttlc.client_id,
        'symbol':'ptt',
        'type':'inmkt_canrec_candle_1d_df',
    },timeout=10)

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print('interapt')
            mqttlc.stop_and_join()
            break