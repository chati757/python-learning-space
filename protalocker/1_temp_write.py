import pickle
import portalocker
import time
import os
import inspect

print(f'pid : {os.getpid()}')

filename = 'tempfile.pkl'
filename_lock = filename+'.lock'

data = {
    'Forest': {'level': -1, 'parent': None, 'children': ['1', '5']},
    '1': {'b': 'test', 'level': 1, 'parent': 'Forest', 'children': ['2', '4']},
    '5': {'b': 'test', 'level': 1, 'parent': 'Forest', 'children': ['6']},
    '2': {'b': '1', 'level': 2, 'parent': '1', 'children': []},
    '4': {'b': 'test', 'level': 2, 'parent': '1', 'children': []},
    '6': {'b': 'test', 'level': 2, 'parent': '5', 'children': []}
}

def try_to_rename_file(filename_lock:str=None,filename:str=None):
    while True:
        try:
            os.rename(filename_lock,filename)
        except PermissionError as e:
            print(f'{inspect.stack()[0].function} : {inspect.stack()[0].linenumber} : PermissionError : {e}')
            time.sleep(1)
            continue
        except KeyboardInterrupt:
            print(f'{inspect.stack()[0].function} : {inspect.stack()[0].linenumber} : KeyboardInterrupt')
            break

if os.path.exists('tempfile.pkl.lock'):
    try_to_rename_file(filename_lock,filename)

while True:
    try:
        with open(filename, 'wb') as file:  # 'rb' หมายถึงอ่านแบบไบนารี
            portalocker.lock(file, portalocker.LOCK_EX)
            pickle.dump(data,file)
            print('lock and writing..15 second')
            time.sleep(15)
            portalocker.unlock(file)
        
        print('temp_write.py standby or do another..15 second')
        time.sleep(15)

    except KeyboardInterrupt:
        print('keyboard interrupt')
        break

print('temp_write exiting..')
try_to_rename_file(filename,filename_lock)
    