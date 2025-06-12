import paho.mqtt.client as mqtt
from datetime import datetime
import threading
import subprocess
import time
import signal
import os
import shutil
import configparser
import json
import pandas as pd

class mqtt_local_client(threading.Thread):
    def __init__(self,config_userpass_file_path=None,username=None,broker_ip=None,broker_port=None,topic='topic/test',mode='both',on_message_func=None):
        if(config_userpass_file_path==None or username==None):
            raise Exception('mqtt_local_client : arguments error : please check config_userpass_file_path and username')
        
        if(mode in ['both','receiver','sender']==False):
            raise Exception('mqtt_local_client : mode error : please check mode')

        if(mode in ['both','receiver']==True):
            raise Exception('mqtt_local_client : on_message_func empty')

        super().__init__()
        self.daemon = True
        self.config = configparser.ConfigParser()
        self.config.read(config_userpass_file_path)
        
        if(broker_ip==None or broker_port==None):
            self.broker_ip = self.config.get('MQTT','broker_address')
            self.broker_port = int(self.config.get('MQTT','broker_port'))
        else:
            self.broker_ip = broker_ip
            self.broker_port = int(broker_port)

        self.username = username
        self.password = self.config.get(self.username,'password')

        if('/' not in topic):
            topic = topic + '/'
        self.topic = topic

        # สร้าง client instance
        self.client = None
        self.client = mqtt.Client()
        # ตั้งค่า username และ password
        self.client.username_pw_set(self.username, self.password)
        # ตั้งค่า callback functions
        self.client.on_connect = self.__on_connect
        self.client.on_disconect = self.__disconnect
        self.rc = None

        self.mode = mode
        if(self.mode=='both' or self.mode=='receiver'):
            #Ex. on_message(client,userdata,msg)
            self.client.on_message = on_message_func

        self.is_ready_work = threading.Event()

    def run(self):
        print(f'mqtt_local_client : {threading.get_ident()} : connecting..')
        # เชื่อมต่อกับ broker
        self.client.connect(self.broker_ip,self.broker_port)
        # เริ่ม loop เพื่อรับและส่งข้อมูล
        self.client.loop_forever()

    def stop(self):
        self.__disconnect()

    def stop_and_join(self):
        self.stop()
        self.join()
        pass

    def __on_connect(self,client,userdata,flags,rc):
        self.rc = rc
        if(self.rc==0):
            self.is_ready_work.set()
            print(f'mqtt_local_client : {threading.get_ident()} : connected')
    
    def subscribe_topic(self,sub_topic:str):
        if(self.rc!=0):
            self.is_ready_work.wait()
            
        self.client.subscribe((self.topic+sub_topic),qos=1)
        print(f'mqtt_local_client : subscribe_topic : {(self.topic+sub_topic)} : subscribed')
        self.is_ready_work.clear()

    def send_data(self,sub_topic:str,json_data):
        if(self.rc!=0):
            self.is_ready_work.wait()
        
        self.client.publish((self.topic+sub_topic),json_data,qos=1)
        self.is_ready_work.clear()

    def __disconnect(self):
        print(f"mqtt_local_client : {threading.get_ident()} : disconnecting from broker...")
        self.is_ready_work.clear()
        self.client.disconnect()

if __name__=='__main__':

    def mqttlc_on_message(client,userdata,msg):
        print(msg.payload.decode())
        df = pd.DataFrame(json.loads(msg.payload.decode()))
        print(df)
        print(df.dtypes)
        pass

    mqttlc = mqtt_local_client(
        config_userpass_file_path='client_userpass.ini',
        username='testuser',
        topic='topic/',
        mode='receiver',
        on_message_func=mqttlc_on_message
    )

    mqttlc.start()
    mqttlc.subscribe_topic(sub_topic='test')

    import pdb;pdb.set_trace()