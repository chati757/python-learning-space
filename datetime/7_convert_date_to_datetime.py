from datetime import datetime

date = datetime.now().date()
print(date)

#combine technique

print(datetime.combine(date,datetime.min.time()))

#or convert time.struct_time and convert to datetime

print(datetime(*datetime.now().date().timetuple()[:6]))