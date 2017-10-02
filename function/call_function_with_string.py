class config_manager():
    def install(self):
          print "In install"

def nonclass_call():
    print("hello non class")

#------------call with class--------------
method_name = 'install'
my_cls = config_manager()
method = getattr(my_cls, method_name)
method()

#------------call non class type-----------
globals()["nonclass_call"]()