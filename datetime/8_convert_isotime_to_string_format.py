import datetime
testdate = '2022-08-26T13:56:14+07:00'
print(datetime.datetime.fromisoformat(testdate).strftime('%Y-%m-%d %H:%M:%S'))