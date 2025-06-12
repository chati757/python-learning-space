import subprocess
import getpass
import os
import configparser
import socket

def create_acl_pw_and_userpass_file():
    acl_file = './acl_file'
    password_file = './pw_file'
    userpass_file = './client_userpass.ini'
    
    while True:
        user = input("Enter the username : ")

        if not user:
            print("Username cannot be empty.")
            continue
        
        password = getpass.getpass("Enter the password : ")
        # Run mosquitto_passwd command เพื่อสร้าง password_file
        #subprocess.run(['mosquitto_passwd', '-c', password_file, user], input=password + '\n' + password + '\n', text=True, check=True)
        if not password:
            print("Error: Empty password.")
            continue

        if(os.path.exists(password_file)==False):
            with open(password_file,'w') as file:
                file.close()

        process = subprocess.Popen(
            ['mosquitto_passwd', '-b', password_file, user,password],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # อ่าน error ที่เกิดขึ้น (ถ้ามี)
        error_output = process.stderr.read()
        if error_output:
            print(f"Failed to create/update password file")
            print("Error encountered:", error_output.strip())
            continue
        else:
            process.stdout.flush()
            print(process.stdout.read())
            print(f"Password for user '{user}' updated successfully.")
            print(f"Password file created/updated successfully for user {user}.")

        topic = input("Enter the topic (default: topic/test) : ")
        if not topic:
            topic = 'topic/test'
        
        if os.path.exists(acl_file):
            with open(acl_file, 'a+') as file:
                file.seek(0)
                if f"user {user}" in file.read():
                    print(f"user : {user} already exists in {acl_file}. please insert another username")
                    continue
                else:
                    file.write(f"\nuser {user}")
                    file.write(f"\ntopic readwrite {topic}")
        else:
            print(f'ACL file path not found , automatic creating ACL file')
            file = open(acl_file, 'w')
            file.write(f"user {user}\n")
            file.write(f"topic readwrite {topic}\n")
            file.close()
            print('create empty acl_file : success')
        
        config = configparser.ConfigParser()
        config['MQTT'] = {
            'broker_address':socket.gethostbyname(socket.gethostname()),
            'broker_port':'1883'
        }

        config[user] = {
            'password':password 
        }

        with open(userpass_file, 'w') as configfile:
            config.write(configfile)

        print('ctrl+c for exist')

if __name__ == "__main__":
    create_acl_pw_and_userpass_file()