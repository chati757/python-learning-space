from bottle import run,get,route,HTTPResponse
import threading
import time
import json


'''
get with javascript
fetch("http://localhost:9000/data").then(res=>res.json()).then(data=>{console.log(data['key'])})
'''
@route('/data',method='GET')
def index():
    data = {'key': 'value'}
    response = HTTPResponse(json.dumps(data), content_type='application/json')
    response.set_header('Access-Control-Allow-Origin',"http://192.168.1.38:8000")
    response.add_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
    response.add_header('Access-Control-Allow-Headers', 'Content-Type')
    #response.add_header('Access-Control-Allow-Origin',"http://192.168.1.38:8000")
    return response

'''
fetch("http://localhost:9000/data2").then(res=>res.json()).then(data=>{console.log(data['msg'])})
'''
@route('/graph/<symbol>',method='GET')
def index2(symbol):
    print(symbol)
    response = HTTPResponse({'msg':'somedata'}, content_type='application/json')
    response.set_header('Access-Control-Allow-Origin',"http://192.168.1.38:8000")
    return response

def start_server():
    run(host="localhost",port=9000,debug=True)

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
