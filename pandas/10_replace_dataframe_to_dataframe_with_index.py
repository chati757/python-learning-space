import pandas as pd
test_df = pd.DataFrame({'a':[1,2,3,4,5],'b':[5,4,3,2,1]})
test_df2 = pd.DataFrame({'a':[99],'b':[99]},index=[2])

df_con = pd.concat([test_df,test_df2],join='inner')
'''
a   b
0   1   5
1   2   4
2   3   3
3   4   2
4   5   1
2  99  99
'''
df_con = df_con.loc[~df_con.index.duplicated(keep='last')]
'''
    a   b 
0   1   5 
1   2   4 
3   4   2 
4   5   1 
2  99  99 
'''
df_con.loc[~df_con.index.duplicated(keep='last')].sort_index()
'''
    a   b 
0   1   5 
1   2   4 
2  99  99 
3   4   2 
4   5   1 
'''

