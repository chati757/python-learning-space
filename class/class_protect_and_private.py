class Student:
    def __init__(self,test_public,test_protect,test_private):
        self.test_public = test_public
        self._test_protect = test_protect
        self.__test_private = test_private

    def call_from_inside_protect(self):
        print(self._test_protect)
    
    def set_from_inside_protect(self,data):
        self._test_protect = data

    def call_from_inside_private(self):
        print(self.__test_private)
        
    def set_from_inside_private(self,data):
        self.__test_private = data

    @property
    def test_protect(self):
        return 'protect call from outside'

    @test_protect.setter
    def test_protect(self,newname):
        print('protect edit from outside')
        pass

std = Student("test public txt","test protect txt",'test private txt')
print('call normal')
print(std.test_public)
std.test_public = 'edit test public txt'
print(std.test_public)

print('call protect')
print(std.test_protect)
std.test_protect = 'edit test protect txt'
print(std.test_protect)
print('use method from class to call')
std.call_from_inside_protect()
std.set_from_inside_protect('edit test protect txt')
std.call_from_inside_protect()
print('try to call direct protect variable')
print(std._test_protect)
print('try to set direct protect variable')
std._test_protect = 'edit2 test protect txt'
print(std._test_protect)

print('call private')
#print(std.test_private) #can not call and set
#print(std.__test_private) #can not call and set
#print(std._test_private) #can not call and set
print('try to call direct private variable')
print(std._Student__test_private)
print('try to set direct private variable')
std._Student__test_private = 'edit test private txt'
print(std._Student__test_private)
