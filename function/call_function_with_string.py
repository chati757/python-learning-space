class config_manager():
    def install(self):
          print('In install')

    def inner1(self):
        print('call inner1')
    
    def inner2(self):
        eval('self.inner1()')

def nonclass_call():
    print("hello non class")

#------------call with class--------------
method_name = 'install'
my_cls = config_manager()
method = getattr(my_cls, method_name)
method()

#------------call non class type-----------
globals()["nonclass_call"]()
# or
locals()["nonclass_call"]()
# or
config_manager().inner2() #call eval

eval('config_manager().inner1()')