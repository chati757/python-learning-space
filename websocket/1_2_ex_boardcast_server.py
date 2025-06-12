import asyncio
import websockets

connected_clients = set()  # เก็บ client ที่เชื่อมต่ออยู่

async def handler(websocket, path):
    # เพิ่ม client ที่เชื่อมต่อเข้ามาใน set
    connected_clients.add(websocket)
    try:
        while True:
            message = await websocket.recv()
            print(f"Received: {message}")

            # ส่งข้อความไปยังทุก client ที่เชื่อมต่ออยู่
            for client in connected_clients:
                await client.send(f"Broadcast: {message}")

    except websockets.exceptions.ConnectionClosed:
        print("Connection closed.")
    finally:
        # ลบ client ที่ตัดการเชื่อมต่อออกจาก set
        connected_clients.remove(websocket)

start_server = websockets.serve(handler, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()