import pickle
import portalocker
import time

# อ่านข้อมูลจากไฟล์ pickle
with open('data.pkl', 'rb') as file:  # 'rb' หมายถึงอ่านแบบไบนารี
    portalocker.lock(file, portalocker.LOCK_SH)
    loaded_data = pickle.load(file)
    print('reading and waiting 15 second..')
    time.sleep(15)

print("Data loaded from 'data.pkl':")
print(loaded_data)