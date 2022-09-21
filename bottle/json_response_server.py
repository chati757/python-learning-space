from bottle import run,route
import threading
import time

@route('/data')
def index():
    return {'msg':'hello'}

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
