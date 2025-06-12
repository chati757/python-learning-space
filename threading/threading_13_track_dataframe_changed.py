import pandas as pd
import threading
import time

class robot(threading.Thread):
    def __init__(self,name,df,change_columns):
        super(robot,self).__init__()
        self.setDaemon(True)

        if 'global_value_changed_event' not in globals():
            raise Exception('global_value_changed_event not created , please ceaate and try again')

        if 'global_lock' not in globals():
            global global_lock
            global_lock = threading.Lock()

        if 'df_result' not in globals():
            global df_result

        df_result = df
        self.name = name
        self.change_columns = change_columns

    def run(self):
        self.change_value_in_df()
        print('end of thread')

    def change_value_in_df(self):
        x = 1
        while True:
            with global_lock:
                time.sleep(5)
                df_result[self.change_columns].iloc[0] = x
                x+=1
                print(f'{self.name} : df changed and delaying..')
                global_value_changed_event.set()

def check_value_change(df,df2):
    result = []
    for col in df.columns:
        if(col in df2.columns):
            if(not df[col].equals(df2[col])):
                result.append({col:df2[col].values[0]})
    
    return result

if __name__=='__main__':
    global global_value_changed_event 
    global_value_changed_event = threading.Event()

    global df_result
    df = pd.DataFrame({'a':[0],'b':[0]})

    r1 = robot('robot1',df.copy(),'a')
    r1.start()

    r2 = robot('robot2',df.copy(),'b')
    r2.start()

    x = 0
    while x<10:
        x+=1
        print('main waiting')
        global_value_changed_event.wait()
        print('receive from robot class')
        print(check_value_change(df,df_result))
        print(df_result)
        df = df_result.copy()
        global_value_changed_event.clear()#ทำให้ wait() กลับมาทำงานใหม่
        print('---')
