from datetime import datetime
from datetime import timezone
from datetime import timedelta

test_date = datetime.now().replace(tzinfo=timezone(timedelta(seconds=25200))).isoformat()
print(test_date) #2022-09-21T15:48:15.171958+07:00 

#add with datetime string
test_date2 = datetime.strptime('2022-09-12','%Y-%m-%d').replace(tzinfo=timezone(timedelta(seconds=25200))).isoformat()
print(test_date2) #2022-09-12T00:00:00+07:00