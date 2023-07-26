import pandas as pd
# prepare time prototyoe
df_time_prototype = pd.read_csv("./data/time_prototype.csv",index_col=False)
'''
0     2022-07-26 10:00:00
1     2022-07-26 10:01:00
2     2022-07-26 10:02:00
3     2022-07-26 10:03:00
...
20    2022-07-26 10:20:00
'''
# prepare data problem
df2 = pd.read_csv('./data/test_datetime_problem.csv',index_col=False)

problem_date_str = df2['date'].iloc[0].split(" ")[0]
#create datetime prototype
df_datetime_prototype = problem_date_str + " " + df_time_prototype['date']
df_datetime_prototype = pd.DataFrame({'date':pd.to_datetime(df_datetime_prototype)})
print(df_datetime_prototype)

# round min data problem
df2['date'] = pd.to_datetime(df2['date'])
problem_datetime_rounded_se = pd.to_datetime(df2['date']).dt.round('min')

#filter not in df2['date']
filer_df = pd.DataFrame({'date':df_datetime_prototype[~df_datetime_prototype['date'].isin(problem_datetime_rounded_se)]['date']})
complete_df = pd.concat([filer_df,df2]).sort_values(by='date').reset_index(drop=True)
print(complete_df[['date','bid1','offer1']])
print(complete_df[['date','bid1','offer1']].dtypes)

#result
'''
                         date          bid1        offer1
0  2022-07-26 10:00:00.000000           NaN           NaN
1  2022-07-26 10:01:00.000000           NaN           NaN
2  2022-07-26 10:02:00.000000           NaN           NaN
3  2022-07-26 10:03:00.000000           NaN           NaN
4  2022-07-26 10:04:00.000000           NaN           NaN
5  2022-07-26 10:05:00.070031  17.0 | 303.3  17.1 | 182.0
6  2022-07-26 10:06:00.068618  17.0 | 307.5  17.1 | 200.4
7  2022-07-26 10:07:00.055096  17.0 | 251.2  17.1 | 349.1
8  2022-07-26 10:08:00.064752   17.0 | 82.9  17.1 | 433.7
9  2022-07-26 10:09:00.071803   17.0 | 94.3  17.1 | 412.8
10 2022-07-26 10:10:00.061853  16.9 | 474.2  17.0 | 107.9
11 2022-07-26 10:11:00.000000           NaN           NaN
12 2022-07-26 10:12:00.000000           NaN           NaN
13 2022-07-26 10:13:00.000000           NaN           NaN
14 2022-07-26 10:14:00.066677  17.0 | 197.5  17.1 | 384.6
15 2022-07-26 10:15:00.060074  17.0 | 192.2  17.1 | 383.6
16 2022-07-26 10:16:00.065853  17.0 | 197.7  17.1 | 389.8
17 2022-07-26 10:17:00.000000           NaN           NaN
18 2022-07-26 10:18:00.000000           NaN           NaN
19 2022-07-26 10:19:00.000000           NaN           NaN
20 2022-07-26 10:20:00.000000           NaN           NaN
'''

#if you need to nan last data
print(complete_df.loc[complete_df['date']<=df2['date'].iloc[-1],['date','bid1','offer1']])