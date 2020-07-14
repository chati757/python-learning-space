def safe_execute(default, exception, function, *args):
    try:
        return function(*args)
    except exception:
        return default

if __name__=='__main__':
    print(safe_execute(0,Exception,(lambda a,b:a+b),2,3))