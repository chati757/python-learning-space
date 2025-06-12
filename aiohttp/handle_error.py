import aiohttp
import asyncio

'''
#ป้องกันการ ไม่สามารถปิด loop ใน window ได้ หากเราสร้าง loop เอง และสั่ง loop.close() อาจเกิด error

#อาการที่แจ้งเตือน
Exception ignored in: <function _ProactorBasePipeTransport...
RuntimeError: Event loop is closed

'''
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def test_fetch():

    url = "https://api.example.com/endpoint"
    headers = {'Accept': 'application/json'}
    params = {'param1': 'value1'}
    
    # ใช้ aiohttp เพื่อส่งคำขอแบบ async
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as response:
                # ตรวจสอบผลลัพธ์และส่งค่า JSON กลับ
                result = await response.json()
                return result  # Return ค่าผลลัพธ์ JSON

    except aiohttp.ClientResponseError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except aiohttp.ClientConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except asyncio.TimeoutError as timeout_err:
        print("The request timed out.")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")