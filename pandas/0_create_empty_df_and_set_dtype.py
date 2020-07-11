import numpy
import pandas as pd

dtypes = numpy.dtype([
          ('a', str),
          ('b', int),
          ('c', float),
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