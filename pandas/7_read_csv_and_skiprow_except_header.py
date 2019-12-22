import pandas as pd

df = pd.read_csv('./data/timeseries.csv',index_col = False,skiprows=range(1,2))
print(df)
'''
 Date   High   Low   Open  Close
0  2017-12-25  87.00  85.0  85.50  85.25
1  2017-12-26  86.50  84.5  85.25  86.25
2  2017-12-27  86.75  85.5  86.50  85.75
3  2017-12-28  85.50  84.0  85.25  85.00
4  2017-12-29  85.25  84.5  85.00  85.00
'''