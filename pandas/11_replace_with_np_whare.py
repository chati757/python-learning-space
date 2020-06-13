import numpy as np
import pandas as pd

df = pd.DataFrame({'date':[1,2,3,4,5],'a':[2,4,5,6,7]})
df2 = pd.DataFrame({'date':[3,4,5,6,7,8],'a':[6,7,8,9,10,11]})

df_merge = pd.merge(df,df2,how='left',on=['date'])
'''
    date  a_x  a_y
0     1    2  NaN
1     2    4  NaN
2     3    5  6.0
3     4    6  7.0
4     5    7  8.0
'''
'''
Ex.np.where(df_merge['a_y'].isna(),df_merge['a_x'],df_merge['a_y'])
Ex.array([2., 4., 6., 7., 8.])
'''
df_merge['a_x'] = np.where(df_merge['a_y'].isna(),df_merge['a_x'],df_merge['a_y'])
'''
   date  a_x  a_y
0     1  2.0  NaN
1     2  4.0  NaN
2     3  6.0  6.0
3     4  7.0  7.0
4     5  8.0  8.0
'''
df_merge.drop(['a_y'],axis=1,inplace=True)
'''
   date  a_x
0     1  2.0
1     2  4.0
2     3  6.0
3     4  7.0
4     5  8.0
'''
