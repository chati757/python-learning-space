#Find the most frequent value in list
#====================================

pre_test_str = "geeks for geeks"
print(pre_test_str.count("geeks"))

pre_test = [1,5,7,5,5]
print(pre_test.count(5)) #result is 3 

test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4] 
print(max(set(test), key = test.count))