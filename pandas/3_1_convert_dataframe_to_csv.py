import datetime
from datetime import timedelta
import pandas_datareader as pdr


print("get stock price in period type")
dataframe = pdr.get_data_yahoo('BCP.BK', start = datetime.datetime.today()-timedelta(days=10), end = datetime.datetime.today()-timedelta(days=1))
print(dataframe)
dataframe.to_csv('test.csv')