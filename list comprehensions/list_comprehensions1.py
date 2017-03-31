def v1():
    for i in range(1,11):
        print(i,i*0.621371192)

#python3 only : list comprehensions
def v2():
   [print(i,i*0.621371192) for i in range(1,11)]
   #m = [(funciton) (loop)]
   m= [i*0.621371192 for i in range(1,11)]
   print(m)

#python3 only : lambda expression type
def v3():
    m = ((lambda i: i * 0.621371192),range(1,11))
    print(m)
#v1()
v2()
#v3()