import threading
import requests
import websocket  # สำหรับการทำงานกับ WebSocket
import time

# HTTP Capability
class HTTPCapability:
    def fetch_data(self, url: str):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        response.raise_for_status()

# WebSocket Capability
class WebSocketCapability:
    def __init__(self, url: str):
        self.url = url
        self.ws = None

    def connect(self):
        self.ws = websocket.create_connection(self.url)
        print("Connected to WebSocket")

    def receive_data(self):
        if self.ws:
            return self.ws.recv()
        return None

    def close_connection(self):
        if self.ws:
            self.ws.close()
            print("WebSocket connection closed")

# Thread สำหรับ HTTP
class MyThread_HTTP(threading.Thread):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.http_capability = HTTPCapability()  # สร้าง HTTPCapability ภายใน

    def run(self):
        print(f"{self.name} starting HTTP task...")
        try:
            data = self.http_capability.fetch_data("https://api.example.com/data")
            print(f"{self.name} fetched HTTP data: {data}")
        except Exception as e:
            print(f"{self.name} HTTP fetch error: {e}")
        print(f"{self.name} finished HTTP task.")

# Thread สำหรับ WebSocket
class MyThread_WebSocket(threading.Thread):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.ws_capability = WebSocketCapability("ws://example.com/socket")  # สร้าง WebSocketCapability ภายใน

    def run(self):
        print(f"{self.name} starting WebSocket task...")
        try:
            self.ws_capability.connect()
            message = self.ws_capability.receive_data()
            print(f"{self.name} received WebSocket message: {message}")
        finally:
            self.ws_capability.close_connection()
        print(f"{self.name} finished WebSocket task.")

# สร้างและรันแต่ละ thread แยกกัน
http_thread = MyThread_HTTP(name="HTTPThread")
ws_thread = MyThread_WebSocket(name="WebSocketThread")

http_thread.start()
ws_thread.start()
http_thread.join()
ws_thread.join()