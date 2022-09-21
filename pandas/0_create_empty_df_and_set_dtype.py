import numpy
import pandas as pd

dtypes = numpy.dtype([
          ('a', str),
          ('b', int),
          ('c', float),#np.float64(np.nan)
          ('d', numpy.datetime64),
          ])
data = numpy.empty(0, dtype=dtypes)
df = pd.DataFrame(data)

print(df)
print(df.dtypes)

#------------------------------------------------------------
se1 = pd.Series(dtype='object')
se2 = pd.Series(dtype='float64')
df2 = pd.DataFrame({'a':se1,'b':se2})

print(df)
print(df.dtypes)

#------------------------------------------------------------
#create with loc
df.loc[:,'require_fixed'] = pd.Series([],dtype='object')
print(df)

#------------------------------------------------------------
#create empty series from dataframe (depend on dtype)
import numpy as np
df3 = pd.DataFrame({'a':[2.2,22.1,5.3],'b':['test1','test2','test3'],'c':[2,3,4]})
se3 = df3.iloc[1].copy()
se3[df3.select_dtypes(include=['float64']).columns] = np.float64(np.nan)
se3[df3.select_dtypes(include=['int64']).columns] = np.float64(np.nan)
se3[df3.select_dtypes(include=['object']).columns] = None
print(se3)
