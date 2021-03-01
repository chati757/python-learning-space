import configparser
import json

config = configparser.ConfigParser()

config.read('config.ini')

print(config['DEFAULT']['test'])
fibs = json.loads(config.get('DEFUALT','fibs'))