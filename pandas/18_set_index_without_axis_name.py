import pandas as pd

df = pd.DataFrame({'symbol':['a','b','c'],'value':[2,3,4]})
#normal : set index
df.set_index('symbol')
'''
#output :
        value
symbol       
a           2
b           3
c           4
'''
#if you need to delete symbol can be delete with df.index.name = None

#or set_index like this (from begin)
df.set_index(pd.Series(df['symbol'].tolist())).drop('symbol',axis=1)
'''
#output
   value
a      2
b      3
c      4
'''