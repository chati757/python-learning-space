def testreceivetuple(a,b,*args):
    print(a,b)
    print(args)

testreceivetuple('a','b',[1,2,3])
#send 5,6 to a,b and send list to tuple
testreceivetuple(*[5,6],[1,2,3])
'''
def testreceivedict(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    print(f'kwargs:{kwargs}')
    print(f'kwargs.values:{kwargs.values}')
    for arg in kwargs.values():
        result += arg
    return result

print(testreceivedict(**{'a':'Real','b':'Python'}))
print(testreceivedict(a="Real", b="Python", c="Is", d="Great", e="!"))

def testpassdict(a,b):
    print(a)
    print(b)

#call with
testpassdict(a='123',b='456')
testpassdict(**{'a':'123','b':'456'})

def testpasstuple(a,b):
    print(a)
    print(b)

#call with
testpasstuple(*(2,3))
testpasstuple(*[2,3])
'''