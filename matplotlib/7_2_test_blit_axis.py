import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.ticker as ticker
import pandas as pd
from datetime import datetime
from datetime import timedelta
import numpy as np
import sys

df = pd.read_csv('ex.csv',index_col=False).head(15)
#add current date
last_index = len(df)
df.loc[last_index,['Date']] = datetime.strftime(datetime.now(),'%Y-%m-%d')
df.loc[last_index,['Open','High','Low','Close']] = 17.4

fig = plt.figure(figsize=[5,5],dpi=100)
#fig.canvas.pan_zoom_throttle = 1000 #ยังไม่ทราบว่าส่งผลในด้านไหนแต่ (คาดว่าช่วยเรื่องการ refresh move/pan)
#fig = plt.figure(figsize=[5,5],tight_layout=True,dpi=100) #อาจทำให้ move/pan อาจกระตุกมากขึ้นได้
fig.suptitle('testing')
mgs = fig.add_gridspec(1, 1) #main grid
sgs = mgs[0].subgridspec(1, 1) #sub grid
ax = fig.add_subplot(sgs[0,0])

#save empty ticklabel background
print('save empty axis')
ax.xaxis.set_major_locator(ticker.NullLocator())
ax.yaxis.set_major_locator(ticker.NullLocator())
plt.pause(3) #make sure fig and axis have rendered
bg = fig.canvas.copy_from_bbox(fig.bbox)

x_trick = []
for c,i in enumerate(df['Date']):
    current_date_int = int(i.split("-")[2])
    if(c>0):
        prev_date_int = int(df.loc[c-1,'Date'].split("-")[2])

        if(prev_date_int<current_date_int):
            x_trick.append(current_date_int)
            continue

        x_trick.append(datetime.strftime(datetime.now(),'%b%d'))
    else:
        x_trick.append(current_date_int)

ax.set_xticks(df.index,rotation=0,ha='center',labels=x_trick)

ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()
y_trick = np.arange(df.Low.min(),df.High.max()+0.1,0.1).round(2)
ax.set_yticks(y_trick,labels=y_trick)

#set back to default ticklabel
ax.xaxis.set_major_locator(ticker.AutoLocator())
ax.set_xlim(-1,17)
fig.canvas.draw_idle()

def fmt(x,y):
    try:
        x = df.Date[(int(x))]
    except:
        x = 'unknown'

    return f"{x},{'%1.2f'%y}"

ax.format_coord = fmt

'''
plot historical data
'''
# find the rows that are bullish
dfup = df[df.Close >= df.Open]
# find the rows that are bearish
dfdown = df[df.Close < df.Open]

width  = 0.7   # width of real body
width2 = 0.1  # width of shadow

# plot the bullish candle stick
ax.bar(dfup.index, dfup.Close - dfup.Open, width, bottom = dfup.Open, edgecolor='g', color='green')
ax.bar(dfup.index, dfup.High - dfup.Close, width2, bottom = dfup.Close, edgecolor='g', color='green')
ax.bar(dfup.index, dfup.Low - dfup.Open, width2, bottom = dfup.Open, edgecolor='g', color='green')
# plot the bearish candle stick
test = ax.bar(dfdown.index, dfdown.Close - dfdown.Open, width, bottom = dfdown.Open, edgecolor='r', color='red')
ax.bar(dfdown.index, dfdown.High - dfdown.Open, width2, bottom = dfdown.Open, edgecolor='r', color='red')
ax.bar(dfdown.index, dfdown.Low - dfdown.Close, width2, bottom = dfdown.Close, edgecolor='r', color='red')

'''
key press event
'''
start_price_change = 0.1
def on_press(event):
    global start_price_change
    sys.stdout.flush()
    if event.key == '1':
        print('set price up')
        current_bar, = ax.bar(15, start_price_change, width,bottom = 17.4, edgecolor='g', color='green')
        print(current_bar)
        #current_bar.set_height(start_price_change)
        #ax.figure.canvas.draw_idle()
        start_price_change+=0.1
        ax.draw_artist(current_bar)
        fig.canvas.blit(ax.bbox)
    elif(event.key =='2'):
        print('change xlim (normal type)')
        ax.set_xlim(1,40)
        fig.canvas.draw()
    elif(event.key =='3'):
        print('change xlim (blit type)(custom tick)')
        fig.canvas.restore_region(bg)
        ax.set_xlim(1,15)
        ax.set_xticks(np.arange(15),labels=np.arange(15))
        print(len(ax.xaxis.get_ticklabels()))
        for i in ax.xaxis.get_ticklabels():
            ax.draw_artist(i)

        for i in ax.xaxis.get_ticklines():
            ax.draw_artist(i)

        fig.canvas.blit(fig.bbox)
    elif(event.key =='4'):
        print('change xlim (blit type)(auto tick)')
        fig.canvas.restore_region(bg)
        ax.set_xlim(1,3)
        ax.xaxis.set_major_locator(ticker.AutoLocator())
        print(len(ax.xaxis.get_ticklabels()))
        for i in ax.xaxis.get_ticklabels():
            ax.draw_artist(i)

        for i in ax.xaxis.get_ticklines():
            ax.draw_artist(i)

        fig.canvas.blit(fig.bbox)


fig.canvas.mpl_connect('key_press_event', on_press)

plt.show()