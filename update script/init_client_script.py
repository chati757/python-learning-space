import json
import requests
import configparser

#prepare config
config = configparser.RawConfigParser()
config.read('client_config.cfg')
#request header
headers = {'User-Agent': 'python'}

#check update and update state
response = requests.get(config.get('server','server_url')+'/version', headers=headers)
if(str(response.json()['version'])!=config.get('version','version')):
    #download and replace main file
    r = requests.get(config.get('server','server_url')+'/download_last_script')
    open(config.get('client','main_filename'), 'wb').write(r.content)    

    #download and replace library
    r2 = requests.get(config.get('server','server_url')+'/download_last_setor_lib')
    open(config.get('client','main_filename'), 'wb').write(r2.content)   

    #update config
    config.set('version', 'version',response.json()['version'])  
    with open('config.cfg', 'w') as configfile:  
        config.write(configfile)

import main_script
