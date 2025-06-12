import asyncio
import asyncio_mqtt

'''
เป็น async ที่ทำงาน 3 task 
task ที่ 3 เป็น mqtt_subscriber ชื่อ mqtt_subscribe_task
task ที่ 2 สามารถ publish กลับไป broker ได้
task ที่ 1 เป็นการทำงาน async แบบธรรมดา
'''

# ตั้งค่า MQTT broker
MQTT_BROKER = 'your_mqtt_broker_address'
MQTT_TOPIC = 'your_topic_name'

async def task1():
    while True:
        print("Task 1 is running...")
        await asyncio.sleep(5)

async def task2(client):
    while True:
        print("Task 2 is running...")
        await asyncio.sleep(3)
        
        # ส่งข้อความไปยัง topic ของ broker
        message = "Hello from Task 2!"
        await client.publish(MQTT_TOPIC, message)
        print(f"Task 2 published message: {message}")

async def mqtt_subscribe_task(client):
    async with client.filtered_messages(MQTT_TOPIC) as messages:
        await client.subscribe(MQTT_TOPIC)
        async for message in messages:
            print(f"Received message on {MQTT_TOPIC}: {message.payload.decode()}")

async def main():
    async with asyncio_mqtt.Client(MQTT_BROKER) as client:
        # รัน tasks ทั้งหมดและส่ง client ไปให้ task2 และ mqtt_subscribe_task ใช้งาน
        await asyncio.gather(
            task1(),
            task2(client),
            mqtt_subscribe_task(client)
        )

# รัน main
try:
    asyncio.run(main())
except asyncio_mqtt.MqttError as error:
    print(f"MQTT error: {error}")