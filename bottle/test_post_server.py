from bottle import run,route,post,request
import threading
import time
import bottle as bt

app = bt.Bottle()
'''
import requests
x = requests.post(url, json = myobj) # send by json type
x = requests.post(url, data = myobj) # send by data type (froms)
'''

@app.post('/test_add_symbol') # or @route('/login', method='POST')
def test_add_symbol():
    #print(request.json['symbol']) # receive json type
    print(request.forms.get('symbol')) # receive data (froms) type
    return {'result':'ok'}

def start_server():
    run(app,host="localhost",port=7000,debug=True)

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