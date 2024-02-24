import pandas as pd
import eel

#function for java state


#------------------------------------

#test dataframe
df = pd.DataFrame({'stock':['ptt','bcp'],'sector':['energy','energy'],'grade':['a','c'],'hlfc':['4','2'],'rsi10':['33.234','30.955'],'rsi_wtb':['6:w.4-5:t.3:tp.2-4(lower)','6:w.4-5:t.3:tp.2-4(lower)'],'inv_harami_pattern':['TRUE','FALSE'],'double_pattern':['FALSE','TRUE']})

eel.init("web")
eel.start("main.html",host="192.168.1.38",block=False)
#calculate rsi10 set100 and get rsi10_val and rsi10_level
#eel.update_set100_rsi10(rsi10_val,rsi10_level)
eel.fetch_table_data(df.to_json(orient="values"))

#test error from javascript (py to js)
def print_num(n):
    print('Got this from Javascript:', n)


def print_num_failed(error, stack):
    print("This is an example of what javascript errors would look like:")
    print("\tError: ", error)
    '''
        Error:  test.something is not a function
    '''
    print("\tStack: ", stack)
    '''
        Stack:  TypeError: test.something is not a function
    at Object.js_with_error (http://192.168.2.36:8000/main.html:136:18)
    at WebSocket.eel._websocket.onmessage (http://192.168.2.36:8000/eel.js:135:82)
    '''

# Show error handling function()(callback,error)
eel.js_with_error()(print_num, print_num_failed)

#test error to javascript (js to py)
@eel.expose
def py_exception(error):
    print(type(error))
    if error:
        raise ValueError("Test")
    else:
        return "No Error"

while True:
    print('active')
    eel.sleep(10)