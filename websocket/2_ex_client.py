import asyncio
import websockets

async def client_task():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        try:
            while True:
                # ส่งข้อความปกติ
                await websocket.send("Hello")
                response = await websocket.recv()
                print(response)

                await asyncio.sleep(10)  # รอระยะเวลาหนึ่ง
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed.")

asyncio.get_event_loop().run_until_complete(client_task())