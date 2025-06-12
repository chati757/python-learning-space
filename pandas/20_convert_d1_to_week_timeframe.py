import pandas as pd
from datetime import datetime
# สร้าง DataFrame จากข้อมูล
data = {
    'Date': ['2023-01-30', '2023-01-31', '2023-02-01', '2023-02-02', '2023-02-05', '2023-02-06', '2023-02-07', '2023-02-08', '2023-02-09', '2023-02-12', '2023-02-13', '2023-02-14', '2023-02-15', '2023-02-16', '2023-02-19', '2023-02-20', '2023-02-21', '2023-02-22', '2023-02-23', '2023-02-26'],
    'Open': [33.25, 33.25, 33.00, 33.00, 32.75, 32.75, 32.75, 32.75, 32.25, 32.25, 32.50, 32.50, 32.75, 32.50, 33.50, 33.00, 33.00, 32.75, 32.50, 32.25],
    'Close': [33.25, 33.25, 33.00, 33.00, 32.75, 32.50, 32.75, 32.50, 32.50, 32.25, 32.75, 32.75, 32.75, 33.50, 33.00, 33.25, 32.75, 32.25, 32.50, 32.00]
}

df = pd.DataFrame(data)

# แปลงชนิดข้อมูลของคอลัมน์ 'Date' เป็น datetime
week_df = df.copy()
week_df['Date'] = pd.to_datetime(week_df['Date'])
week_df['week_label'] = week_df['Date'].dt.year.astype(str).str[:4]+week_df['Date'].dt.isocalendar().week.astype(str)
week_acc_df = week_df.groupby('week_label').agg({'Close':'max'}).reset_index()

#(week timeframe) merge week to date
import pdb;pdb.set_trace()
week_df = pd.merge(week_df.groupby('week_label').tail(1),week_acc_df,on='week_label',how='left')
print(week_df)
import pdb;pdb.set_trace()
'''
การแปลง week แบบนี้จะแตกต่างจากตัวอย่าง 19_group_data_by_datetime.py เพราะจะอิงข้อมูล date ตาม df เดิมที่มีอยู่
เช่นข้อมูลเดิมมี mon , tue , thu การ merge จะอ้างอิง thu เป็นตัวแทนของสัปดาห์นั้นแทน ไม่สร้างวันศุกร์ (fri) ขึ้นมาใหม่
'''