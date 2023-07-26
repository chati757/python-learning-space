import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from datetime import datetime

plt.style.use("Solarize_Light2")
#plt.style.use('ggplot')

def zigzag(df):
    df['zigzag'] = pd.Series([],dtype="float64")
    deviation_percent = 0.02
    current_higher_high_state = None
    last_extremum_index = None
    last_high = 0
    last_low = 0
    start_close = df.loc[0,'Close']
    for i in range(1,len(df)):
        buff_close = df.loc[i,'Close']
        #check positive change
        buff_percent_chg = (buff_close-start_close)/start_close
        if(buff_close>start_close and buff_percent_chg>deviation_percent):
            if(current_higher_high_state==True):
                df.loc[last_extremum_index,'zigzag'] = None
            start_close = buff_close
            df.loc[i,'zigzag'] = df.loc[i,'High']
            last_high = df.loc[i,'High']
            current_higher_high_state = True
            last_extremum_index = i
        #check negative change
        elif(buff_close<start_close and buff_percent_chg<(-deviation_percent)):
            if(current_higher_high_state==False):
                df.loc[last_extremum_index,'zigzag'] = None
            start_close = buff_close
            df.loc[i,'zigzag'] = df.loc[i,'Low']
            last_low = df.loc[i,'Low']
            current_higher_high_state = False
            last_extremum_index = i
        else:
            #track last high or low
            if(current_higher_high_state==True and df.loc[i,'High']>=last_high):
                df.loc[i,'zigzag'] = df.loc[i,'High']
                df.loc[last_extremum_index,'zigzag'] = None
                last_extremum_index = i
            elif(current_higher_high_state==False and df.loc[i,'Low']<=last_low):
                df.loc[i,'zigzag'] = df.loc[i,'Low']
                df.loc[last_extremum_index,'zigzag'] = None
                last_extremum_index = i


    return df

def calc_add_current_b_band(hist_df,buff_se,period:int=2):
    if(period<0 or period>len(hist_df)):
        raise Exception('ind_b_band : error period (out of range)')
    
    if(all([i in hist_df.columns for i in ['b_band_x_bar','b_band_top','b_band_bottom']])==False):
        raise Exception('ind_b_band : Open , High , Low , Close columns incomplete')

    if(all([i in buff_se.keys() for i in ['Open','High','Low','Close']])==False):
        raise Exception('ind_b_band : Open , High , Low , Close columns incomplete')

    buff_se['b_band_x_bar'] = pd.Series(hist_df['Close'].iloc[-(period-1):].tolist()+[buff_se['Close']]).mean()
    std_buff = pd.Series(hist_df['Close'].iloc[-(period-1):].tolist()+[buff_se['Close']]).std(ddof=1)*2
    buff_se['b_band_top'] = buff_se['b_band_x_bar'] + std_buff
    buff_se['b_band_bottom'] = buff_se['b_band_x_bar'] - std_buff

    return buff_se

df = pd.read_csv('ex.csv',index_col=False)
period=50
df['b_band_x_bar'] = df['Close'].rolling(period).mean()
df['b_band_top'] = df['b_band_x_bar']+(df['Close'].rolling(period).std(ddof=1)*2)
df['b_band_bottom'] = df['b_band_x_bar']-(df['Close'].rolling(period).std(ddof=1)*2)

#df = df.copy()[81:160]
df = df.copy()
df = zigzag(df)
#print(df[['Close','b_band_x_bar','b_band_top','b_band_bottom']])
#print(calc_add_current_b_band(df[:299],df.iloc[-1],50))

#create figure
fig = plt.figure()
fig.tight_layout()
ax = fig.add_subplot(111)

#define width of candlestick elements
width = .9
width2 = .05

#define up and down df
up = df[df.Close>=df.Open]
down = df[df.Close<df.Open]

#define colors to use
col1 = 'green'
col2 = 'red'

#plot up df
ax.bar(up.index,up.Close-up.Open,width,bottom=up.Open,color=col1)
ax.bar(up.index,up.High-up.Close,width2,bottom=up.Close,color=col1)
ax.bar(up.index,up.Low-up.Open,width2,bottom=up.Open,color=col1)

#plot down df
ax.bar(down.index,down.Close-down.Open,width,bottom=down.Open,color=col2)
ax.bar(down.index,down.High-down.Open,width2,bottom=down.Open,color=col2)
ax.bar(down.index,down.Low-down.Close,width2,bottom=down.Close,color=col2)

#----------plot line-----------
ln1, = ax.plot(df.index,df.b_band_top,color='black')
ln2, = ax.plot(df.index,df.b_band_x_bar,color='black')
ln3, = ax.plot(df.index,df.b_band_bottom,color='black')
ln4, = ax.plot(df.loc[df['zigzag'].isna()!=True,'zigzag'].index,df.loc[df['zigzag'].isna()!=True,'zigzag'],color='red')


#rotate x-axis tick labels
#ax.set_xticks(df.Date,rotation=45, ha='right',labels=df.Date)
plt.xticks(rotation=45)
ax.xaxis.set_major_locator(ticker.AutoLocator())
#ln1.set_visible(False)
#ln2.set_visible(False)

#x_date = [f'{df.Date[i]}' for i in np.arange(0,len(df),20)]
#print(x_date)
#ax.set_xticks(x_date)

#display candlestick chart
plt.show()