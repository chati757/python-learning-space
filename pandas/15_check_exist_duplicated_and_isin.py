import pandas as pd

df = pd.DataFrame({'a':[1,2,2,9,1],'b':[9,2,2,5,0]})
'''
   a  b
0  1  9
1  2  2
2  2  2
3  9  5
4  1  0
'''

df.duplicated()
'''
0    False
1    False
2     True
3    False
4    False
'''

df.isin([9])
'''
0  False   True
1  False  False
2  False  False
3   True  False
4  False  False
'''