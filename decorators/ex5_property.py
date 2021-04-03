class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    
    @property #property ทำให้เราเรียก .email ได้โดยไม่ต้อง .email()
    def email(self):
        return '{}.{}@email.com'.format(self.name,self.last)

    @property #property ทำให้เราเรียก .fullname ได้ด้วยไม่ต้องเรียก .fullname()
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first , last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('delete name from deleter')
        self.first = None
        self.last = None

emp_1 = Employee('John','Smith')
print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)

#use setting
print('\nafter setter')
emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)

#use deleter
print('\nafter deleter')
del emp_1.fullname