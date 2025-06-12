import paho.mqtt.client as mqtt
from datetime import datetime
import threading
import subprocess
import time
import signal
import os
import shutil
import psutil
import configparser
import inspect
import queue
import json

class mqtt_local_broker(threading.Thread):
    def __init__(self,broker_config_file_path,persistence_db_file_path,persistence_backup_dir,debug_mode=False):
        if(os.path.isfile(broker_config_file_path)!=True or os.path.isfile(persistence_db_file_path)!=True or os.path.isdir(persistence_backup_dir)!=True):
            raise Exception(f'mqtt_local_broker : {threading.get_ident()} : error\n please check broker_config_file_path , persistence_db_file_path , self.persistence_backup_dir')
        
        super().__init__()
        self.daemon = True
        self.broker_process = None
        self.debug_mode = debug_mode
        self.broker_config_file_path = broker_config_file_path
        self.persistence_db_file_path = persistence_db_file_path
        self.persistence_backup_dir = persistence_backup_dir

    def run(self):
        self.__broker_start_thread()

    def stop(self):
        self.__broker_stop_thread()

    def stop_and_join(self):
        self.stop()
        self.join()

    def __broker_start_thread(self):
        print(f'mqtt_local_broker : {threading.get_ident()} : starting')
        if(self.debug_mode==True):
            self.broker_process = subprocess.Popen(["mosquitto","-c",self.broker_config_file_path,"-v"])
        else:
            self.broker_process = subprocess.Popen(["mosquitto","-c",self.broker_config_file_path])
        self.broker_process.wait()

    def __broker_stop_thread(self):
        print(f'mqtt_local_broker : {threading.get_ident()} : stoping')
        if self.broker_process:
            # Send SIGINT to the broker process
            os.kill(self.broker_process.pid, signal.SIGINT)
        
        self.__backup_broker_persistence_data()

    def __backup_broker_persistence_data(self):
        print(f'mqtt_local_broker : {threading.get_ident()} : backup_broker_persistence_data : checking..')
        max_size = 10000000

        # ตรวจสอบว่าไฟล์ db มีอยู่หรือไม่
        if os.path.isfile(self.persistence_db_file_path):
            # ตรวจสอบขนาดของไฟล์
            file_size = os.path.getsize(self.persistence_db_file_path)
            
            if file_size > max_size:
                # สร้าง timestamp
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_file = os.path.join(self.persistence_backup_dir, f"mosquitto_{timestamp}.db").replace('\\','/')
                
                # ย้ายไฟล์ไปที่ backup
                shutil.move(self.persistence_db_file_path, backup_file)
                
                # สร้างไฟล์ใหม่
                open(self.persistence_db_file_path, 'w').close()
                print(f'mqtt_local_broker : {threading.get_ident()} : backup_broker_persistence_data : success')

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
        self.client_ip = None
        try:
            self.client_ip = [addrs[1].address for interface, addrs in psutil.net_if_addrs().items() if(interface=='Ethernet')][0]
        except IndexError:
            raise IndexError('cannot get ethernet ip address')

        self.thread_id = threading.get_ident()
        self.client_id = self.client_ip+':'+inspect.stack()[-1].filename.split('\\')[-1]
        self.client = mqtt.Client(self.client_id)
        # ตั้งค่า username และ password
        self.client.username_pw_set(self.username, self.password)
        # ตั้งค่า callback functions
        self.retry_to_connect = 5
        self.client.on_connect = self.__on_connect
        self.client.on_disconect = self.__disconnect
        self.rc = None

        self.mode = mode
        if(self.mode=='both' or self.mode=='receiver'):
            #Ex. on_message(client,userdata,msg)
            self.client.on_message = on_message_func

        self.is_ready_work = threading.Event()
        self.get_response_queue = queue.Queue()
        self.lock_get_request = threading.Lock()
        self.subscribe_topic_list = []

    def run(self):
        print(f'mqtt_local_client : {threading.get_ident()} : connecting..')
        # เชื่อมต่อกับ broker
        while True:
            try:
                self.client.connect(self.broker_ip,self.broker_port)
                break
            except ConnectionRefusedError:
                print(f'mqtt_local_client : {threading.get_ident()} : connection refused error')
                if(self.retry_to_connect<=1):
                    print(f'mqtt_local_client : {threading.get_ident()} : thread stop')
                    self.is_ready_work.clear()
                    exit()
                self.retry_to_connect-=1
                time.sleep(3)

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
            print(f"client id : {self.client_id}")

    def subscribe_topic(self,sub_topic:str):
        if(self.rc!=0):
            self.is_ready_work.wait(timeout=60)

        self.client.subscribe((self.topic+sub_topic),qos=1)
        print(f'mqtt_local_client : {threading.get_ident()} : subscribe_topic : {(self.topic+sub_topic)} : subscribed')
        self.subscribe_topic_list.append((self.topic+sub_topic))
        self.is_ready_work.clear()

    def publish_topic(self,sub_topic:str,json_data):
        if(self.rc!=0):
            self.is_ready_work.wait(timeout=60)

        self.client.publish((self.topic+sub_topic),json_data,qos=1,retain=False)
        self.is_ready_work.clear()

    def mqtt_get_request(self,request_data,timeout=10):
        if(not (self.topic+'get_response/'+self.client_id) in self.subscribe_topic_list):
            print(f'mqtt_local_client : {threading.get_ident()} : mqtt_get_request : error \n{request_data}')
            print(f"please check subscribe {(self.topic+'get_response/'+self.client_id)} already or not")
        elif(not 'client_id' in request_data.keys() or request_data['client_id'] in ['',None]):
            print(f'mqtt_local_client : {threading.get_ident()} : mqtt_get_request : error \n{request_data}')
            print(f"please check request data : requst data not client_id")
        else:
            with self.lock_get_request:
                self.client.publish((self.topic+'get_request'),json.dumps(request_data),qos=1)
                print(f'mqtt_local_client : {threading.get_ident()} : mqtt_get_request : sent \n{request_data}')
                try:
                    response = self.get_response_queue.get(timeout=timeout)
                    return response
                except queue.Empty:
                    print(f'mqtt_local_client : {threading.get_ident()} : mqtt_get_request : error : request timeout\n{request_data}')
                    return 'Request timed out'

    def __disconnect(self):
        print(f"mqtt_local_client : {threading.get_ident()} : disconnecting from broker...")
        self.is_ready_work.clear()
        self.client.disconnect()