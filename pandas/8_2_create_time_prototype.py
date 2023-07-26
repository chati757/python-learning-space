import pandas as pd
# prepare data prototyoe
df = pd.read_csv('./data/test_datetime_prototype.csv',index_col=False)
'''
0     2022-07-26 10:00:00.029204
1     2022-07-26 10:01:00.066942
2     2022-07-26 10:02:00.068793
3     2022-07-26 10:03:00.054395
...
20     2022-07-26 10:20:00.059411
'''
# round min data prototype
df['date'] = pd.to_datetime(df['date']).dt.round('min').dt.strftime("%H:%M:%S") #or round('T')
df['date'].to_csv('./data/time_prototype.csv',index=False)