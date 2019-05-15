import pandas as pd

data_series = pd.Series(['cp','cd','cd','cp','cd','cp'])
print(data_series)

dataframe=data_series.to_frame()
print(dataframe.loc[dataframe[0]=='cp'])