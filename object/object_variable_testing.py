
test = {"t1":"test1","t2":"test2"}


keys = test.keys()
values = test.values()
 
print(keys) #dict_keys(['t1','t2'])
print(values) #dict_values(['test1','test2'])

print("list key")
print(list(keys)) #['t1','t2']
print("list key : specify type")
print(list(keys)[0]) #t1
print("list value")
print(list(values)) #['test1','test2']
print(list(values)[0]) #test1

print("get value t1")
print(test.get('t1')) #test1
print("update value")
test.update({"t1":"test3"})
print(list(values)) #['test1','test2']
print(test.get('t1')) #test3

'''
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> a == b == c == d == e
True
'''