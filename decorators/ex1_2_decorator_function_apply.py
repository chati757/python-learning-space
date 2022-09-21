import pandas as pd

def decorator_func(func):
    print('call @decorator')
    def wrap_func(*arg):
        def wrap2_func(result):
            print('do something in wrap2 before return')
            return result
        print(f'running : {func.__name__}')
        return wrap2_func(func(*arg))
    return wrap_func

@decorator_func
def test_func(df):
    print(df)
    print('in test func')
    return 2,3

df = pd.DataFrame({'a':[2,3,4]})
print(test_func(df))
