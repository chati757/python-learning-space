from bottle import run,route,request,static_file,get,post
import threading
import time
import some_routine
import pandas as pd

@route('/version')
def version():
    #test_data : call global variable
    print(global_share_data_obj['data1'])
    print(global_share_data_obj['data2'])
    print(request.headers.get('User-Agent'))
    print(some_routine.share_num)
    return {'version':0.0}

@route('/download_last_script')
def last_script():
    return static_file('init_client_script.py',root='.', download='test_init_client_script.py')

#@get('/testre/<symbol:re:^\w{1,13}$>/<price:re:^\d{1,4}[.]\d{2}$>')
@get('/testre/<symbol:re:\w{1,13}>/<price:re:\d{1,4}[.]\d{2}>')
def testre(symbol,price):
    print(symbol)
    print(price)

'''
import requests
url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj) # send by json type
x = requests.post(url, data = myobj) # send by data type (froms)
'''

@post('/test_add_symbol') # or @route('/login', method='POST')
def test_add_symbol():
    #print(request.json['symbol']) # receive json type
    print(request.forms.get('symbol')) # receive data (froms) type
    return {'result':'ok'}

def start_server():
    run(host="192.168.2.38",port=7000,debug=True)

if __name__ == '__main__':
    try:
        threading.Thread(target=start_server,daemon=True).start()
        while True:
            time.sleep(1)
            #print('server is running')
    except KeyboardInterrupt:
        # never reached
        print('server closed')