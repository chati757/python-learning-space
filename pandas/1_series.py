import pandas as pd

data_series = pd.Series([20,12,18,10])
print(data_series)
"""
0    20
1    12
2    18
3    10
dtype: int64
"""
print(data_series[0])
"""
20
"""
print(data_series[1:])
"""
1    12
2    18
3    10
dtype: int64
"""
print(data_series[1:3]) # 3 is exclusive
"""
1    12
2    18
dtype: int64
"""
print(data_series*3)
"""
0    60
1    36
2    54
3    30
dtype: int64
"""
print(data_series.index) # display index size
"""
RangeIndex(start=0,stop=4,step=1)
"""
print(data_series.sum()) # sum all data in series
"""
60
"""
print(data_series.mean())
"""
15.0
"""

ex1 = pd.Series([20,12,18,10],index=[['jan','feb','mar','apr']]) #index setting
print(ex1)
"""
jan    20
feb    12
mar    18
apr    10
dtype: int64
"""