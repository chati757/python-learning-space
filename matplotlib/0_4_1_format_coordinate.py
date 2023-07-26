import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
from datetime import datetime 
#plt.style.use("Solarize_Light2")

width  = 0.7   # width of real body
width2 = 0.1  # width of shadow

# add a row containing the indices of each row
plt.style.use('ggplot')
df = pd.read_csv('ex.csv',index_col=False).head(10)
last_index = len(df)
df.loc[last_index,['Date']] = datetime.strftime(datetime.now(),'%Y-%m-%d')
df.loc[last_index,['Open','High','Low','Close']] = None

#df.set_index(pd.DatetimeIndex(pd.to_datetime(df['Date'])),inplace=True)
#df.set_index(pd.DatetimeIndex(pd.to_datetime(df['Date'])),inplace=True)
#df.set_index(dates.date2num(df['Date']),inplace=True)
#print(df[['Open','High','Low','Close']])

fig, ax = plt.subplots(figsize=(6,6),dpi=100)

def fmt(x,y):
    try:
        x = df.Date[(int(x))]
    except:
        x = 'unknown'

    return f"{x},{'%1.2f'%y}"

ax.format_coord = fmt

# find the rows that are bullish
dfup = df[df.Close >= df.Open]
# find the rows that are bearish
dfdown = df[df.Close < df.Open]
# plot the bullish candle stick
ax.bar(dfup.index, dfup.Close - dfup.Open, width,
       bottom = dfup.Open, edgecolor='g', color='green')
ax.bar(dfup.index, dfup.High - dfup.Close, width2, 
       bottom = dfup.Close, edgecolor='g', color='green')
ax.bar(dfup.index, dfup.Low - dfup.Open, width2, 
       bottom = dfup.Open, edgecolor='g', color='green')
# plot the bearish candle stick
ax.bar(dfdown.index, dfdown.Close - dfdown.Open, width, 
       bottom = dfdown.Open, edgecolor='r', color='red')
ax.bar(dfdown.index, dfdown.High - dfdown.Open, width2, 
       bottom = dfdown.Open, edgecolor='r', color='red')
ax.bar(dfdown.index, dfdown.Low - dfdown.Close, width2, 
       bottom = dfdown.Close, edgecolor='r', color='red')

#rotate x-axis tick labels
plt.xticks(df.index,rotation=45, ha='right')
#import pdb;pdb.set_trace()
#ax.set_xticks(df[::5].index)
ax.set_xlim(-1,12)
ax.set_xticklabels(df['Date'])
plt.show()