def decorator_func(func):
    print('call @decorator')
    def wrap_func():
        print(f'running : {func.__name__}')
        return func()
    return wrap_func

@decorator_func
def test_func():
    print('in test func')

@decorator_func
def test_func2():
    print('in test func2')

test_func2()
test_func()