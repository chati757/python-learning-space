import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import AutoLocator
import numpy as np


df = pd.read_csv(f"P:/project w/project-deeptune_ver3/symbol_hist_csv/ptt.bk.csv",index_col=False)[:10]
#df['Date'] = df['Date'].astype('datetime64[ns]')

fig, ax = plt.subplots(figsize=(10,6),dpi=100)

# สร้างกราฟ
ax.plot(df.index, df.Close, marker='o', linestyle='-') #use df.index for plot axis

#import pdb;pdb.set_trace()
ax.set_xticks([i for i in df.index]) #fix UserWarning
ax.set_xticklabels(df['Date']) #for display date string format
ax.xaxis.set_major_locator(AutoLocator())

# กำหนดชื่อแกน x และ y
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# กำหนดชื่อกราฟ
plt.title('example')

#ในส่วนการแสดง coordinate มุมบนขวา หากไม่ได้กำหนดส่วนนี้จะเป็นค่าว่าง set ax.format_coord ขึ้นมา 
xlim_arr = ax.get_xlim()
def fmt(x,y):
    try:
        #x = df.Date[int(((x-xlim_arr[0])-4))] #0.6976744 = 60/86 (60 is len(df.Date) , 86 is len of trick on graph)
        x = df.Date[int((x-xlim_arr[0])+0.55)] # -0.45 + 1 = 0.55 
    except:
        x = 'unknown'

    return f"{x},{'%1.2f'%y}"

ax.format_coord = fmt

print(df.Date)

# แสดงกราฟ
plt.show()