class decorator_class(object):
    def __init__(self,original_function):
        print('on init')
        print(original_function.__name__)
        self.original_function = original_function

    def __call__(self,*args,**kwargs):
        print('call method executed in class')
        return self.original_function(*args,**kwargs)

print('before first')
@decorator_class #decorator_class(display)
def display(name,age):
    print('in display function')
    print('in display',name,age)

print('\ncall first')
print(display) #<function decorator_function.<locals>.wrap_function at 0x000002724369BCA8>
print('\ncall second')
display('name','age')