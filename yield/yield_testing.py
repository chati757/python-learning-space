#yield function
#yield is a generator and return iterator
def ex_yield():
    print("in function yield")
    yield 2
    #when print 2 in function print(p) back to ex_yield() function for work next yield is yield(3) in ex_yield function
    yield 3
    yield 10
    yield 11

#no no yield function
def ex_noyield():
    print("in function no yield")
    print("2")
    print("3")

#call stage-------------------------------------
nump=0
numi=0
# no error call function and work all line in function
for p in ex_yield():
    nump+=1
    print("loop number ex_yield is ",nump)
    print(p)

# just call the function ex_noyield and error occured
for i in ex_noyield():
    numi+=1
    print("loop number ex_noyield is ",numi)
    print(i)