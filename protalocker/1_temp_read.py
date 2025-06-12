import pickle
import portalocker
import time
import os

print(f'pid : {os.getpid()}')

filename = 'tempfile.pkl'
filename_lock = filename+'.lock'

def waiting_lock_file():
    while os.path.exists(filename_lock):
        try:
            print('waiting..file unlock')
            time.sleep(1)
        except KeyboardInterrupt:
            print('keyboard interrupt')
            exit()

waiting_lock_file()

while True:
    try:
        with open(filename, 'rb') as file:  # 'rb' หมายถึงอ่านแบบไบนารี
            portalocker.lock(file, portalocker.LOCK_SH)
            loaded_data = pickle.load(file)
            print('lock and reading..15 second')
            print(loaded_data)
            time.sleep(15)
            portalocker.unlock(file)
        
        print('temp_read.py standby or do another..15 second')
        time.sleep(15)

    except KeyboardInterrupt:
        print('keyboard interrupt')
        break

    except FileNotFoundError:
        waiting_lock_file()
        continue

    