'''
import pandas as pd
#ex dataframe
    rsi_rate       comment
0     17.650           NaN
1     18.750           NaN
2     25.000           NaN
3     31.175           NaN
4     35.000  sub_red_zone
5     36.500  sub_red_zone
6     37.500  sub_red_zone
7     44.000  sub_red_zone
8     45.000           NaN
9     48.000           NaN
10    55.000           NaN
11    56.125           NaN
12    60.000           NaN
13    62.500           NaN
14    66.000           NaN
15    68.750           NaN
16    74.000           NaN
17   100.000           NaN

pd.isna(df.loc[4,'comment']) # False
pd.isna(df.loc[3,'comment']) # True
'''
 