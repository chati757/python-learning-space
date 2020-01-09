import pandas as pd

#concat and merge if the index is the same
df = pd.DataFrame({'index':[2,3,4,5],'a':[2,2,2,2]})
df2 = pd.DataFrame({'index':[1,4,6,7],'b':[5,5,5,5]})
df_con = pd.concat([df,df2],sort=False)
df_con.drop_duplicates(subset='index',keep=False).append(pd.merge(df,df2,on='index')).sort_values(by='index')

'''
#output : 
       index    a    b
    0      1  NaN  5.0
    0      2  2.0  NaN
    1      3  2.0  NaN
    0      4  2.0  5.0
    3      5  2.0  NaN
    2      6  NaN  5.0
    3      7  NaN  5.0
'''