import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.ticker as ticker
import pandas as pd

fig_width = 7
fig_height = 5
bar_width = .3
bar_width_shadow = .03

fig = plt.figure(figsize=[fig_width,fig_height],tight_layout=False,dpi=100)
#fig.suptitle('testing')

#main grid
mgs = fig.add_gridspec(nrows=1,ncols=1) #main grid

#sub grid
sgs1 = mgs[0].subgridspec(nrows=1,ncols=7,wspace=1, hspace=0.0)

#ax
ax1 = fig.add_subplot(sgs1[:,:6])
ax1.set_title('intraday')
ax1.set_ylabel('price',labelpad=-5)
ax1.set_xlabel('time')

ax1t1 = ax1.twinx()
#ax1t1.spines.left.set_position(("axes",-0.15))
ax1t1.spines["left"].set_position(("axes", -0.1))
ax1t1.yaxis.tick_left()
ax1t1.yaxis.set_label_position("left")
ax1t1.set_ylabel('volume(M.)',labelpad=5)

ax2 = fig.add_subplot(sgs1[:,-1:])
ax2.set_ylabel('price',labelpad=-5)
ax2.set_title('candle')

df = pd.DataFrame({'x':[1, 2, 3, 4, 5, 6, 7],'y':[1, 2, 2, 4, 3, 4, 3],'eyb':[0, 300, 0, -500, 0, -700, 0],'eyt':[-200, 0, 400, 0, -600, 0, 800]})

max_volume_chg = df[['eyb','eyt']].abs().max().max()
diff_max_min_price = (df['y'].max()-df['y'].min())
df['eyb'] = (df['eyb']/max_volume_chg)*diff_max_min_price #remain negative state (incase value is negative)
df['eyt'] = (df['eyt']/max_volume_chg)*diff_max_min_price #remain negative state (incase value is negative)

ax1.errorbar(df.index,df.y,[[0]*len(df),df.eyt.abs()],fmt='o',markersize=0,ecolor=df['eyt'].apply(lambda x:'g' if(x>=0) else 'r'))
ax1.errorbar(df.index,df.y,[df.eyb.abs(),[0]*len(df)],fmt='o',markersize=0,ecolor=df['eyb'].apply(lambda x:'g' if(x>=0) else 'r'))
ax1.plot(df.index,df.y,color='b')

if(df.y.iloc[-1]>df.y.iloc[0]):
    bar_color = 'g'
else:
    bar_color = 'r'

ax2.bar(0, df.y.iloc[-1]-df.y.iloc[0], bar_width, bottom=df.y.iloc[0], color=bar_color)
ax2.bar(0, df.y.max()-df.y.iloc[-1], bar_width_shadow, bottom=df.y.iloc[-1], color=bar_color)
ax2.bar(0, df.y.min()-df.y.iloc[0], bar_width_shadow, bottom=df.y.iloc[0], color=bar_color)
ax2.xaxis.set_major_locator(ticker.NullLocator())
ax2.set_ylim((ax2.get_ylim()[0]-(ax2.get_ylim()[1]/2)),ax2.get_ylim()[1])

plt.show()
