import asyncio
import threading
from paho.mqtt.client import AsyncClient

# สร้าง MQTT Client
mqtt_client = AsyncClient()
client_lock = threading.Lock()  # สร้าง Lock

async def async_publish(client, topic, message):
    # ใช้ lock เพื่อป้องกันการเข้าถึงพร้อมกัน
    with client_lock:
        await client.publish(topic, message)
        print(f"Published message '{message}' to topic '{topic}'")

def thread_function(loop, client, topic, message):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(async_publish(client, topic, message))

# สร้าง Event Loop สำหรับแต่ละ Thread
loop_a = asyncio.new_event_loop()
loop_b = asyncio.new_event_loop()

# สร้าง Threads
thread_a = threading.Thread(target=thread_function, args=(loop_a, mqtt_client, "topic_a", "Message A"))
thread_b = threading.Thread(target=thread_function, args=(loop_b, mqtt_client, "topic_b", "Message B"))

# เริ่ม Threads
thread_a.start()
thread_b.start()

# รอให้ Threads ทำงานเสร็จ
thread_a.join()
thread_b.join()