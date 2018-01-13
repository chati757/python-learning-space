#example of import

#basic import import [module] 
import math
print("basic import")
print(math.pow(2,3))
 
#can be define custom module name 
import math as mh
print("import as")
print(mh.pow(2,4))

#can be specify function or all function (*) in module
#from [module] import [specify function or *(all function can use)] 
#from math import pow,log,..[some another function in math]
from math import pow
print("import specify type")
print(pow(2,2))

#advance import
#from math import pow as pw,log as lg..[some another function in math]
from math import pow as pw
print("advance type")
print(pw(2,5))

module = __import__('math')
func = getattr(module,'pow')
func()