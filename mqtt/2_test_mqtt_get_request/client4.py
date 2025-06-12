import asyncio
from asyncio_mqtt import Client, MqttError
import json

async def mqtt_request(broker, request_topic, response_topic, request_payload, lock, queue, timeout=10):
    """ฟังก์ชันหลักที่รับผิดชอบในการส่ง Request และรับ Response"""
    async def publish_request():
        """Publish ข้อความไปที่ Request Topic"""
        async with Client(broker) as client:
            await client.publish(request_topic, json.dumps(request_payload))

    async with lock:  # ใช้ Lock สำหรับการป้องกันการทำงานซ้ำ
        # เริ่มต้น Task สำหรับการรอข้อความ
        queue.put_nowait(None)  # Reset queue ก่อนเริ่ม
        tasks = [
            asyncio.create_task(publish_request())
        ]

        try:
            # รอข้อความตอบกลับจาก Queue ภายในเวลา Timeout
            response_message = await asyncio.wait_for(queue.get(), timeout=timeout)
            return response_message
        except asyncio.TimeoutError:
            raise TimeoutError("No response received within the timeout period")
        finally:
            for task in tasks:
                task.cancel()  # ยกเลิก Task ทั้งหมดเมื่อเสร็จสิ้น

async def handle_message(broker, response_topic, queue):
    """Handle message จาก Queue ภายนอก mqtt_request"""
    try:
        async with Client(broker) as client:
            await client.subscribe(response_topic)
            async with client.messages() as messages:
                async for msg in messages:
                    topic = msg.topic
                    payload = msg.payload.decode()
                    if topic == response_topic:
                        # ส่งข้อความไปที่ queue
                        await queue.put(payload)
    except asyncio.CancelledError:
        pass

async def main():
    broker = "localhost"
    request_topic = "request/topic"
    response_topic = "response/topic"
    request_payload = {"key":"value"}

    queue = asyncio.Queue()  # สร้าง Queue สำหรับรับข้อความ
    lock = asyncio.Lock()  # สร้าง Lock สำหรับการป้องกันการใช้งานหลายครั้ง

    # สร้าง task สำหรับ handle_message ที่ทำงานต่อเนื่อง
    message_handler_task = asyncio.create_task(handle_message(broker, response_topic, queue))

    try:
        response = await mqtt_request(broker, request_topic, response_topic, request_payload, lock, queue)
        print("Response received:", response)
    except TimeoutError as e:
        print(e)
    finally:
        message_handler_task.cancel()  # หยุด message handler เมื่อเสร็จ

if __name__ == "__main__":
    asyncio.run(main())
