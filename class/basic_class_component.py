class MyClass:
    class_var:int = 1 # is a class attribute

    def __init__(self, i_var):
        #Constructor area
        self.i_var = i_var # is an instance attribute:

foo = MyClass(2)
bar = MyClass(3)

print(foo.class_var, foo.i_var)# 1, 2
print(bar.class_var, bar.i_var)# 1, 3
print(MyClass.class_var)# 1
print(MyClass.i_var)# erorr