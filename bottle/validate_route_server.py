from bottle import run,route,get
import threading
import time


'''
import requests
requests.get("http://localhost:7000/testre/asdb/12.23")
'''

#@get('/testre/<symbol:re:^\w{1,13}$>/<price:re:^\d{1,4}[.]\d{2}$>')
@get('/testre/<symbol:re:\w{1,13}>/<price:re:\d{1,4}[.]\d{2}>')
def testre(symbol,price):
    print(symbol)
    print(price)

def start_server():
    run(host="localhost",port=7000,debug=True)

def start_with_thread():
    try:
        threading.Thread(target=start_server,daemon=True).start()
        while True:
            time.sleep(1)
            #print('server is running')
    except KeyboardInterrupt:
        # never reached
        print('server closed')

if __name__ == '__main__':
    start_with_thread()