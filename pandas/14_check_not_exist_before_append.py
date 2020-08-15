import pandas as pd 

df = pd.DataFrame({'a':[1,2,2,1,1],'b':[9,2,2,9,9]})

'''
   a  b 
0  1  9 
1  2  2 
2  2  2 
3  1  9 
4  1  9 
'''

#if it's exist it's pass and not append
try: 
    df.loc[len(df)] = {'a':1,'b':9} if(df.append({'a':1,'b':9},ignore_index=True).duplicated().any()==False) else []
except ValueError:
    print('inexcept')
    pass

print(df)