from bottle import route, run, request
import requests

@route('/')
def proxy():
    # กำหนด URL ของเว็บไซต์ปลายทาง
    target_url = 'https://httpbin.org/' + request.fullpath

    # ส่งคำขอ GET ไปยังเว็บไซต์ปลายทาง
    response = requests.get(target_url)

    # ส่งคำตอบกลับไปยังเบราว์เซอร์
    return response.content

if __name__ == '__main__':
    # กำหนด IP และพอร์ตของเซิร์ฟเวอร์
    run(host='localhost', port=9000)