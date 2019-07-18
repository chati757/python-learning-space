#Check the memory usage of objects
#=================================

import sys

a = 1
x = sys.getsizeof(a)
print(x)