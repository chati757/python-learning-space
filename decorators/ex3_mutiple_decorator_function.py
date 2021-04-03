def decorator_function(original_function):
    print('decorator func')
    print('  do another before call '+original_function.__name__+'()')
    def wrap_function(*arg):
        print('  wrap func')
        print('    check arg of '+original_function.__name__+'()')
        print('    call original function '+original_function.__name__+'()')
        return original_function(*arg)
    return wrap_function


def decorator_function2(original_function):
    print('decorator func2')
    print('  do another before call '+original_function.__name__+'()')
    def wrap_function(*arg):
        print('  wrap func2')
        print('    check arg of '+original_function.__name__+'()')
        print('    call original function '+original_function.__name__+'()')
        return original_function(*arg)
    return wrap_function

print('before first')
@decorator_function #decorator_display = decorator_function(original_function) ;decorator_deisplay()
@decorator_function2 #decorator_display2 = decorator_function2(original_function) ;decorator_deisplay2()
'''
เริ่มจาก decorator_function2 ก่อน
decorator_function(decorator_function2(display))
'''
def display(name,age):
    print('in display function')
    print('in display',name,age)

'''
decorator_function2 จะทำงานก่อน และค่อย ครอบด้วย decorator_function อีกที
'''