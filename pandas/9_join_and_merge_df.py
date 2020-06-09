import pandas as pd

df = pd.DataFrame({'date':[1,2,3,4,5],'a':[2,4,5,6,7]})
'''
#output:
    date a
0     1  2
1     2  4
2     3  5
3     4  6
4     5  7
'''
df2 = pd.DataFrame({'date':[3,4,5],'b':[6,7,8]})
'''
#output:
    date b
0     3  6
1     4  7
2     5  8
'''
print(df.join(df2.set_index('date'),on='date'))
'''
#output:
    date a   b
0     1  2  NaN
1     2  4  NaN
2     3  5  6.0
3     4  6  7.0
4     5  7  8.0
'''
print(pd.merge(df,df2,on='date',how='outer'))
'''
#output:
    date a   b
0     1  2  NaN
1     2  4  NaN
2     3  5  6.0
3     4  6  7.0
4     5  7  8.0
'''
print(pd.merge(df,df2,on='date',how='inner'))
'''
#output:
date  a  b
0     3  5  6
1     4  6  7
2     5  7  8
'''