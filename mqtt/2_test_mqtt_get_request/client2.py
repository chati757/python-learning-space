import paho.mqtt.client as mqtt
import threading
import json

# สร้าง Event สำหรับรอผลลัพธ์
response_event = threading.Event()
response_message = None  # ตัวแปรเก็บผลลัพธ์

def on_message(client, userdata, msg):
    global response_message
    topic = msg.topic
    payload = msg.payload.decode()

    # ตรวจสอบว่าเป็นข้อความตอบกลับที่ต้องการหรือไม่
    if topic == "response/topic":
        response_message = payload  # เก็บข้อความตอบกลับ
        response_event.set()  # ปล่อย Event เพื่อบอกว่ามีข้อความตอบกลับแล้ว

def mqtt_request(client, request_payload):
    global response_message

    # รีเซ็ตค่าของ Event และผลลัพธ์
    response_event.clear()
    response_message = None

    # Publish ข้อความไปยัง Request Topic
    client.publish("request/topic", json.dumps(request_payload))

    # รอข้อความตอบกลับ (มี timeout เพื่อป้องกันการรอนานเกินไป)
    if response_event.wait(timeout=10):  # รอไม่เกิน 10 วินาที
        return response_message  # คืนข้อความตอบกลับ
    else:
        raise TimeoutError("No response received within the timeout period")

def main():
    # สร้าง MQTT Client
    client = mqtt.Client()
    client.on_message = on_message  # กำหนด Callback สำหรับรับข้อความ

    # เชื่อมต่อกับ Broker
    client.connect("localhost", 1883, 60)

    # Subscribe หัวข้อที่ใช้ฟังผลลัพธ์
    client.subscribe("response/topic")

    # เริ่ม Loop
    client.loop_start()

    try:
        # ส่งคำขอและรอผลลัพธ์
        request_payload = {"key": "value"}
        response = mqtt_request(client, request_payload)
        print("Response received:", response)
    except TimeoutError as e:
        print(e)

    # หยุด Loop และปิดการเชื่อมต่อ
    client.loop_stop()
    client.disconnect()

if __name__ == "__main__":
    main()
