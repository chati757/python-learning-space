from datetime import datetime

def convert_str_time(strtime) -> 'datetime.now().replace(hour=int(str_hour),minute=int(str_minute),second=int(str_second),microsecond=0)':
    str_hour,str_minute,str_second = strtime.split(':')
    return datetime.now().replace(hour=int(str_hour),minute=int(str_minute),second=int(str_second),microsecond=0)

def dec_check_run_before_datetime(check_datetime):
    if(isinstance(check_datetime,datetime)==False):
        raise Exception('decorator : @check_run_before_datetime : error : argument not datetime format')
    def on_dec(func):
        def on_call(*args):
            if(datetime.now()<check_datetime):
                return func(*args)
            else:
                raise Exception(f'decorator : @check_run_before_datetime : error : block : datetime.now > {datetime.strftime(check_datetime,"%H:%M:%S")}')
        return on_call
    return on_dec

def dec_check_run_after_datetime(check_datetime):
    if(isinstance(check_datetime,datetime)==False):
        raise Exception('decorator : @check_run_before_datetime : error : argument not datetime format')
    def on_dec(func):
        def on_call(*args):
            if(datetime.now()>check_datetime):
                return func(*args)
            else:
                raise Exception(f'decorator : @check_run_before_datetime : error : block : datetime.now > {datetime.strftime(check_datetime,"%H:%M:%S")}')
        return on_call
    return on_dec

@dec_check_run_after_datetime(convert_str_time('22:28:00'))
def test(a,b):
    print(f'on test {a},{b}')

test('a','b')

