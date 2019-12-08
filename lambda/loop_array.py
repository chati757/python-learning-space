#ref : https://caisbalderas.com/blog/iterating-with-python-lambdas/ 
import sys #for check memory

x = [2, 3, 4, 5, 6]
y = [v * 5 for v in x if v % 2]

print(y) #[15, 25]

x = [2, 3, 4, 5, 6]
y = [v * 2 for v in x if v > 5]

print(y) #[12]

x = [2, 3, 4, 5, 6]
lambda x : x*2

x = [2, 3, 4, 5, 6]
f1 = [v * 5 for v in x] 
print(f1) #[10, 15, 20, 25, 30]
f2 = [v for v in x if v > 5]
print(f2) #[6]

#lambda cond.
f = lambda v : True if (v>0) else False
print(f(1))
print(f(-1))

x_rate = {
        'very bad':-0.4,
        'bad':-0.1334,
        'fair':0.1334,
        'good':0.4,
        'very good':999 # more than good
    }
x = 0.1
rate_keys = map(lambda x_rate : x_rate , x_rate)
print(list(rate_keys)) #['very bad', 'bad', 'fair', 'good', 'very good']

rate_values = map(lambda x_rate : x_rate , x_rate.values())
print(list(rate_values)) #[-0.4, -0.1334, 0.1334, 0.4, 999]

#pass x to compare x_rates
print(sys.getsizeof(list(x_rate.keys())[[c for c,i in enumerate(list(x_rate.values())) if x < i][0]]))
print(list(x_rate.keys())[[c for c,i in enumerate(list(x_rate.values())) if x < i][0]]) #fair

def test(x_rate,x):
    res = None
    for c,i in enumerate(x_rate.values()):
        if(x<i):
            res = list(x_rate.keys())[c]
            break
    return res
print(sys.getsizeof(test(x_rate,x)))
print(test(x_rate,x))