#weight_distribution (WD)
#or
#finding low desity (FLD)

import numpy as np
import pandas as pd

xy_train_obj = {30:[31,24],50:[51,47,48],70:[77,68]}

print([i for i in xy_train_obj])
'''
[30, 50, 70]
'''

print([j for i in xy_train_obj for j in [np.array(xy_train_obj[i])]])
'''
[array([31, 24]), array([51, 47, 48]), array([77, 68])]
'''

x_test = 37 #testing input 
x_test_buff = x_test + 1  #shift input

buff_d = [np.sqrt(np.sum((j-(x_test_buff))**2)) for i in xy_train_obj for j in [np.array(xy_train_obj[i])]]
print(buff_d)
'''
[15.652475842498529, 18.708286933869708, 49.20365840057018]
Ex.15.652475842498529 เกิดจาก [31,24]
'''

print(list(xy_train_obj.keys())[buff_d.index(min(buff_d))]) 
'''
30
'''