import requests

url = "https://api.example.com/endpoint"
headers = {'Accept': 'application/json'}
params = {'param1': 'value1'}

try:
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # ยก HTTPError หากมีสถานะ error 4xx หรือ 5xx
    data = response.json()       # ดึงข้อมูล JSON เมื่อไม่มี error
    print(data)
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")