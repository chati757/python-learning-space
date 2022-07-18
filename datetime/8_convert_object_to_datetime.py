import pandas as pd
from datetime import datetime

df = pd.DataFrame({'date':pd.Series([datetime.now()],dtype='object')})
print(df)
'''
                         date
0  2022-07-18 13:27:44.890920
'''

#convert object > pandas datetime > datetime
print(pd.to_datetime(df['date'])[0].to_pydatetime())
print(pd.to_datetime(df['date'])[0].to_pydatetime().hour)