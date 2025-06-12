import os
import shutil

# รับพาธที่สคริปต์ทำงานอยู่
base_path = os.path.dirname(os.path.abspath(__file__))

# กำหนดไฟล์คอนฟิก
config_file_prototype_path = './prototype/mosquitto_prototype.conf'
new_config_file_path = './mosquitto.conf'

# กำหนดพาธเก่าและพาธใหม่
old_path = '<current_path>'
new_path = base_path.replace('\\', '/') # เปลี่ยนเป็นลักษณะพาธแบบ UNIX

# อ่านไฟล์คอนฟิก
with open(config_file_prototype_path, 'r' ,encoding='utf-8') as file:
    config_data = file.read()

# แทนที่พาธเก่าด้วยพาธใหม่
updated_config_data = config_data.replace(old_path, new_path)

# เขียนข้อมูลที่แก้ไขแล้วกลับไปยังไฟล์คอนฟิก
with open(new_config_file_path, 'w' ,encoding='utf-8') as file:
    file.write(updated_config_data)

print(f'Path has been created in {new_config_file_path}')

if(os.path.exists('./client_userpass.ini')==False):
    shutil.copy('./prototype/client_userpass_prototype.ini','./client_userpass.ini')
    print('create client_userpass.ini , please edit broker_ip_address and password')