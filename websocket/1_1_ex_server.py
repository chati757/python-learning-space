import asyncio
import websockets

async def keep_alive(websocket):
    while True:
        await websocket.ping()  # Server ส่ง ping ทุกๆ 30 วินาที
        await asyncio.sleep(30)

async def handler(websocket, path):
    # เริ่ม task keep-alive แยกจากการรับข้อความ
    asyncio.create_task(keep_alive(websocket))

    try:
        while True:
            # รอรับข้อความจาก client
            message = await websocket.recv()
            print(f"Received: {message}")
            '''
            การส่งข้อความกลับไปจะส่งกลับไปแค่ client ที่เราได้รับ message จาก websocket.recv() เท่านั้น
            หากอยากให้ตอบกลับทุก client พร้อมกัน (ดูตัวอย่าง 1_2_ex_boardcast_server.py)
            '''
            await websocket.send(f"Response: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed.")

start_server = websockets.serve(handler, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()