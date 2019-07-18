#Avoid IF
#--------

import time

mydict = {'p':1, 'y':1, 't':1, 'h':1, 'o':1, 'n':1}
word = 'pythonisveryfast'

start = time.time()
for w in word:
    if w not in mydict:
        mydict[w] = 0
    mydict[w] += 1
print(mydict)
print("Time elapsed for IF case is:", time.time() - start)

start = time.time()
for w in word:
    try:
        mydict[w] += 1
    except KeyError:
        mydict[w] = 1

print(mydict)
print("Time elapsed for non-IF case is:", time.time() - start)