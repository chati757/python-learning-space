class dog:
    #constructor 
    #ex gender = famale < it's class variable
    def __init__(self,name,age):
        #slef name < it's instance variable
        self.name = name
        self.age = age
        self.data = None
 
    def say_hello(self):
        print 'Hello, my name is', self.name
        self.data = 8+3
 
    def say_age(self):
        print 'I am', self.age, 'years old'
        return 5

#create object a
a = dog("dang",2)
a.say_hello()
dataa=a.say_age()
print dataa# value form return
print a.data# value form function say_hello pass by constructor

b = dog("duk",4)
b.say_hello()
b.say_age()

#no declare object type 
dog.name = "momo"
dog.say_hello()

test1, test2 = ["test2","test1"]

print(test1)
print(test2)