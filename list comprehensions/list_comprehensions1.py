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

'''
#another example
#backward listing
test = [1,2,3,4,5]
print(test[::-1]) #[5,4,3,2,1]
print([i for i in reversed(test)]) #[5,4,3,2,1]

#sum for each value
period = 14
sum([i+1 for i in range(period)])/period

#condition example
arr = [1,2,3,4,5,6]

#if state
[i for i in arr if i > 2]
#[3, 4, 5, 6]

#if else state
[i if i > 2 else i+1 for i in arr]
#[2, 3, 4, 5, 6]
'''

#get last continue and positive only
#Ex [1,2,-3,-4,5] -> [1,2] (positive and last continue)
arr = [1,2,-3,-4,5]
[arr[j] for c,j in enumerate([arr.index(i) for i in arr if(i>0)]) if(j==c)]
#[1, 2]