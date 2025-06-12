import asyncio
from asyncio_mqtt import Client, MqttError
import json

async def mqtt_request(broker, request_topic, response_topic, request_payload, timeout=10):
    response_event = asyncio.Event()
    response_message = None  # ตัวแปรสำหรับเก็บผลลัพธ์

    async def message_handler():
        """Subscribe และรอข้อความจาก Response Topic"""
        nonlocal response_message
        async with Client(broker) as client:
            try:
                await client.subscribe(response_topic)
                '''
                #เป็นการรับข้อความทุกข้อความโดยไม่ต้องสนว่าจะได้ subscribe ไว้หรือไม่ (ซึ่งกรณีนี้เราไม่ได้ใช้)
                async with client.unfiltered_messages() as messages:
                    async for msg in messages:
                        topic = msg.topic
                        payload = msg.payload.decode()
                        if topic == response_topic:
                            response_message = payload  # เก็บข้อความตอบกลับ
                            response_event.set()  # ตั้ง Event เพื่อปลุก Task ที่รออยู่
                            break
                '''
                async with client.messages() as messages:
                    async for msg in messages:
                        topic = msg.topic
                        payload = msg.payload.decode()
                        if topic == response_topic:
                            response_message = payload  # เก็บข้อความตอบกลับ
                            response_event.set()  # ตั้ง Event เพื่อปลุก Task ที่รออยู่
                            break
            except asyncio.CancelledError:
                await client.disconnect()  # ถ้า task ถูก cancel, disconnect ทันที
                raise

    async def publish_request():
        """Publish ข้อความไปที่ Request Topic"""
        async with Client(broker) as client:
            await client.publish(request_topic, json.dumps(request_payload))

    # รันทั้งสอง Task พร้อมกัน
    tasks = [
        asyncio.create_task(message_handler()),
        asyncio.create_task(publish_request()),
    ]

    try:
        # รอ Event พร้อม Timeout
        await asyncio.wait_for(response_event.wait(), timeout=timeout)
        return response_message
    except asyncio.TimeoutError:
        raise TimeoutError("No response received within the timeout period")
    finally:
        for task in tasks:
            task.cancel()  # ยกเลิก Task ทั้งหมดเมื่อเสร็จสิ้น

async def main():
    broker = "localhost"
    request_topic = "request/topic"
    response_topic = "response/topic"
    request_payload = {"key": "value"}

    try:
        response = await mqtt_request(broker, request_topic, response_topic, request_payload)
        print("Response received:", response)
    except TimeoutError as e:
        print(e)

if __name__ == "__main__":
    asyncio.run(main())
