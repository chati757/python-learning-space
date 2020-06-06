#basic get content array position
test_array =[['Hello', 'World1'], ['How', 'are', 'you?'], ['Bye', 'World2']]
print("all array")
print(test_array)
print("array parser")
print(test_array[2][1][0]) # output is [w] form World2
print(test_array[0][1]) #world1

print("test string[x:x]")
teststr="hello"
print(teststr[:-1])
