from datetime import datetime, timedelta

'''
input : 2022-03

result : [datetime.datetime(2022, 3, 1, 0, 0), datetime.datetime(2022, 3, 31, 0, 0)]
'''
def get_start_and_end_days(date_str):
    result = [datetime.strptime(date_str+'-01',"%Y-%m-%d")]
    buffer_end_date = result[0].replace(day=28) + timedelta(days=4)
    result.append(buffer_end_date - timedelta(days=buffer_end_date.day))
    return result

target_datetime_str = '2022-06'
get_start_and_end_days(target_datetime_str)

import pdb;pdb.set_trace()