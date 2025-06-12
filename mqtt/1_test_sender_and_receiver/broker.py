from datetime import datetime
import threading
import subprocess
import time
import signal
import os
import shutil
import configparser

class mqtt_local_broker(threading.Thread):
    def __init__(self,broker_config_file_path,persistence_db_file_path,persistence_backup_dir):
        if(os.path.isfile(broker_config_file_path)!=True or os.path.isfile(persistence_db_file_path)!=True or os.path.isdir(persistence_backup_dir)!=True):
            raise Exception('error path config please check : broker_config_file_path , persistence_db_file_path , self.persistence_backup_dir')
        
        super().__init__()
        self.daemon = True
        self.broker_process = None
        self.broker_config_file_path = broker_config_file_path
        self.persistence_db_file_path = persistence_db_file_path
        self.persistence_backup_dir = persistence_backup_dir

    def run(self):
        self.__broker_start_thread()

    def stop(self):
        self.__broker_stop_thread()

    def stop_and_join(self):
        #threading.current_thread()
        self.stop()
        self.join()

    def __broker_start_thread(self):
        print('broker_start_thread : starting')
        self.broker_process = subprocess.Popen(["mosquitto","-c",self.broker_config_file_path,"-v"])
        self.broker_process.wait()

    def __broker_stop_thread(self):
        print('broker_stop_thread : stoping')
        if self.broker_process:
            # Send SIGINT to the broker process
            #print(f'process broker id : {self.broker_process.pid}')
            os.kill(self.broker_process.pid, signal.SIGINT)
            #subprocess.run(["taskkill", "/F", "/PID",str(self.broker_process.pid)])

        self.__backup_broker_persistence_data()

    def __backup_broker_persistence_data(self):
        print('backup_broker_persistence_data : checking..')
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
                print('backup_broker_persistence_data : success')

if __name__=='__main__':
    mqttlb = mqtt_local_broker(
        broker_config_file_path='./mosquitto.conf',
        persistence_db_file_path='./persistence_data/mosquitto.db',
        persistence_backup_dir='./persistence_data/'
    )

    mqttlb.start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            mqttlb.stop_and_join()
            break