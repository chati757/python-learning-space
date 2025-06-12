'''
ตัวอย่างการทำ keep alive เพื่อบอกกับ broker ว่ายังไม่ได้ disconnect และยังตงทำงานอยู่
การตั้ง LWT ในส่วน will_set จะเป็นการ publish ข้อความนั้นเมื่อเมื่อ client ดังกล่าว disconnect 
โดยหลักการทำงานของ LWT คือการฝากข้อความและ topic ไว้กับ broker ตั้งแต่ครั้งแรกที่ connect สำเร็จ
โดย broker จะพิจารณาจาก keepalive ของ broker และ keepalive ของ client ว่ายังคงอยู่ในช่วงเวลา
ที่กำหนดหรือไม่ หากเลยจากช่วงที่กำหนดและไม่ได้มีการตอบสนอง broker ก็จะส่งข้อความที่ LWT ที่ client ได้
ฝากเอาไว้

ปล.ปกติการตั้ง keepalive ของ broker ควรมากกว่า keepalive ของ client เพื่อให้การทำงาน
สอดคล้องกัน มิฉะนั้น broker อาจเข้าใจผิดเนื่องจากเลยเวลาที่ควรตอบสนองจึงเข้าใจว่า client นั้น disconnect
แล้วซึ่งจริงๆ client ยังคง connect เพียงแต่ keepalive ช้าจนไม่สอดคล้องส่งผลให้ broker เข้าใจผิดได้
'''

import paho.mqtt.client as mqtt
import time

# Callback เมื่อเชื่อมต่อสำเร็จ
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully!")
        # Subscribe topic test/lwt เพื่อตรวจสอบการ publish
        client.subscribe("test/lwt")
    else:
        print(f"Connection failed with code {rc}")

# Callback เมื่อได้รับข้อความ
def on_message(client, userdata, msg):
    print(f"Message received on {msg.topic}: {msg.payload.decode()}")

# สร้าง client object
client = mqtt.Client()

# ตั้งค่า LWT
client.will_set(topic="test/lwt", payload="Disconnected unexpectedly", qos=1, retain=True)

# กำหนด callback
client.on_connect = on_connect
client.on_message = on_message

# เชื่อมต่อกับ broker
broker_address = "broker.emqx.io"  # เปลี่ยนตาม broker ที่ใช้
port = 1883
client.connect(broker_address, port)

# เริ่ม loop
client.loop_start()

# Publish ข้อความไปยัง topic `test/lwt`
time.sleep(2)  # รอให้เชื่อมต่อสำเร็จ
client.publish("test/lwt", payload="Client is still active", qos=1, retain=False)

# จำลองการทำงานปกติ
time.sleep(5)

# ปิดโปรแกรม (disconnect ปกติ)
print("Disconnecting...")
client.disconnect()
client.loop_stop()
