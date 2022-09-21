from bottle import run,route
import pandas as pd
import threading
import time

'''
import requests
import pandas as pd
import json
from tabulate import tabulate
json_res = requests.get("http://localhost:7000/data").content
df = pd.DataFrame(json.loads(json_res))
print(tabulate(df,showindex=False,headers=df.columns,numalign="left",tablefmt="fancy_outline")+"\n")
'''

@route('/data')
def index():
    df = pd.DataFrame({'a':[2,3,4],'b':[2,3,4]})
    return df.to_json(orient="records") #df.to_json() #can be receive too

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
