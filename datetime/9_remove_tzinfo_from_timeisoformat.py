from datetime import datetime

print(datetime.fromisoformat('2017-05-26T00:00:00+07:00'))
#datetime.datetime(2017, 5, 26, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=25200)))
print(datetime.fromisoformat('2017-05-26T00:00:00+07:00').replace(tzinfo=None))
#datetime.datetime(2017, 5, 26, 0, 0)