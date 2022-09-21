import bottle
from bottle import run,abort
import threading
import time

'''
return error with normal response
'''
@bottle.error(404)
def not_allowed(error):
    print('from 404')
    return "Not accept"

'''
return error with HTTPError instances
'''
@bottle.route("/restricted/<anypath:path>")
def restricted(anypath): 
    print(anypath)
    return bottle.HTTPError(status=406, body='No url specified')

@bottle.route("/restricted2")
def restricted2():
    bottle.abort(404)

@bottle.route("/restricted3")
def restricted3():
    try:
        raise_406 = True #try to change true or false
        print('try something and error but need to return 406 instead of 404')
        if(raise_406==True):
            raise Exception("406")
        else:
            raise Exception("another error code")
        #do not typing bottle.abort(406) on this if you need to abort mutiple case Ex. abort(406),abort(404),and etc.
        #if you typing bottle.abort(406) on this it's not abort but go to exception and abort under (except Exception as e:) instead
    except Exception as e:
        if(str(e)=="406"):
            bottle.abort(406)
        else:
            #another error code
            bottle.abort(404)

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