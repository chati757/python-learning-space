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
#--------------------------------------------loop in loop---------------------------------------------
pos = [[0, 1, 2], [7, 8], [10], [14, 15]]
print([j for i in pos for j in i]) #[0, 1, 2, 7, 8, 10, 14, 15]
#-----------------------------------------------------------------------------------------------------

#--------------------------------------------rate analyze---------------------------------------------
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
#-----------------------------------------------------------------------------------------------------
#---------------------------------group continue of array---------------------------------------------
'''
input = [9,4,1,4,6,1]
#filter < 5
af = [4,1,4,1] 
#convert to index
[c for c,i in enumerate(af)] #[1,2,3,5] --> arrx:[1,2,3,5] --> result:[[1,2,3],[5]] --> last_result:[[4,1,4],[1]]
'''
#[0,1,2,7,8,9,10,13,14,15] --> [[0,1,2],[7,8,9,10],[13,14,15]]
arrx = [0,1,2,7,8,9,10,13,14,15]

arry = arrx.copy()[1:] + [None] #[1,2,7,8,9,10,13,14,15,None]

arrxy = list(map(lambda arrx,arry: [arrx,arry],arrx,arry)) #[[0, 1], [1, 2], [2, 7], [7, 8], [8, 9], [9, 10], [10, 13], [13, 14], [14, 15], [15, None]]

arrxy_filter = list(filter(lambda x: x[0]+1 != x[1], arrxy)) #[[2,7],[10,13],[15,None]]

#arrxy_reduce_dimention = [i[0] for i in arrxy_filter] + [i[1] for i in arrxy_filter] #[2, 10, 15, 7, 13, None]

arrxy_reduce_dimention = [i[0]+i[1] for i in [arrxy_filter[:-1]]][0] #[2, 7, 10, 13]
arrxy_reduce_dimention = [arrx[0]] + arrxy_reduce_dimention + arrx[:-1] #[0, 2, 7, 10, 13, 15]

#marge range from pair of array
even_arr = [i for c,i in enumerate(arrxy_reduce_dimention) if c%2==0]#[0, 7, 13]

odd_arr = [i for c,i in enumerate(arrxy_reduce_dimention) if c%2!=0]#[2, 10, 15]

re = list(map(lambda x,y:[x,y],even_arr,odd_arr))#[[0, 2], [7, 10], [13, 15]]

result = [arrx[arrx.index(i[0]):(arrx.index(i[1])+1)] for i in re] #[[0, 1, 2], [7, 8, 9, 10], [13, 14, 15]]
#-----------------------------------------------------------------------------------------------------
#-------------------------group continue of array (var.2)---------------------------------------------
#[0,1,2,7,8,9,10,13,14,15] --> [[0,1,2],[7,8,9,10],[13,14,15]]
arrx = [0,1,2,7,8,10,14,15]

arry = arrx.copy()[1:] + [None] #[1,2,7,8,9,10,13,14,15,None]

end = [i for c,i in enumerate(arrx) if(arrx[c]+1)!=arry[c]] #[2, 10, 15]

start = [0] + [arrx[c+1] for c,i in enumerate(arrx) if (arrx[c]+1)!=arry[c] and arry[c]!=None] #[0, 7, 13]

re = list(map(lambda x,y:[x,y],start,end))#[[0, 2], [7, 10], [13, 15]]

result = [arrx[arrx.index(i[0]):(arrx.index(i[1])+1)] for i in re] #[[0, 1, 2], [7, 8, 9, 10], [13, 14, 15]]

print([j for i in pos for j in [result]]) #[[0, 1, 2], [7, 8, 9, 10], [13, 14, 15]]
'''
#syntax compression
arrx = [0,1,2,7,8,10,14,15]
arry = arrx.copy()[1:] + [None]
[arrx[arrx.index(i[0]):(arrx.index(i[1])+1)] for i in list(map(lambda x,y:[x,y],([0] + [arrx[c+1] for c,i in enumerate(arrx) if (arrx[c]+1)!=arry[c] and arry[c]!=None]),([i for c,i in enumerate(arrx) if(arrx[c]+1)!=arry[c]])))]
'''
#-----------------------------------------------------------------------------------------------------
#-----------------filter continue in minimum range of array (var.2)-----------------------------------
'''
input = [4,3,1,6,7,8,4,3,9,1,7,8,9,3,1]
#example : filter < 5
output = [[4, 3, 1], [4, 3], [1], [3, 1]]
'''
inputx = [4,3,1,6,7,8,4,3,9,1,7,8,9,3,1]
arrx = [c for c,i in enumerate(inputx) if i<5] # [0, 1, 2, 6, 7, 9, 13, 14]

arry = arrx.copy()[1:] + [None] # [1, 2, 6, 7, 9, 13, 14, None]

end = [i for c,i in enumerate(arrx) if(arrx[c]+1)!=arry[c]] #[2, 7, 9, 14]

start = [0] + [arrx[c+1] for c,i in enumerate(arrx) if (arrx[c]+1)!=arry[c] and arry[c]!=None] #[0, 6, 9, 13]

re = list(map(lambda x,y:[x,y],start,end))#[[0, 2], [6, 7], [9, 9], [13, 14]]

result = [inputx[(i[0]):((i[1])+1)] for i in re] #[[4, 3, 1], [4, 3], [1], [3, 1]]

'''
#syntax compression
inputx = [4,3,1,6,7,8,4,3,9,1,7,8,9,3,1]
arrx = [c for c,i in enumerate(inputx) if i<5] # [0, 1, 2, 6, 7, 9, 13, 14]
arry = arrx.copy()[1:] + [None]
[inputx[i[0]:(i[1]+1)] for i in list(map(lambda x,y:[x,y],([0] + [arrx[c+1] for c,i in enumerate(arrx) if (arrx[c]+1)!=arry[c] and arry[c]!=None]),([i for c,i in enumerate(arrx) if(arrx[c]+1)!=arry[c]])))]
'''
#-----------------------------------------------------------------------------------------------------