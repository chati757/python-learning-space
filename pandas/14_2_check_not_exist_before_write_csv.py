import pandas as pd

df = pd.DataFrame({'a':[1,2,9,1],'b':[9,2,5,0]})
'''
   a  b
0  1  9
1  2  2
2  9  5
3  1  0
'''
try:
   df = pd.read_csv('./data/test_write.csv',index_col=False)
except FileNotFoundError:
   df = pd.DataFrame({'a':[],'b':[]})
   pd.DataFrame({'a':[],'b':[]}).to_csv('./data/test_write.csv')

'''
ตรวจสอบก่อนเขียนลง dataframe ว่า {'a':2,'b':2} ซ้ำหรือไม่ ถ้าซ้ำไม่เขียนลง
'''
try:
   df.append({'a':2,'b':2},ignore_index=~df.append({'a':2,'b':2},ignore_index=True).duplicated().any()).to_csv('./data/test_write.csv',index=False)
except TypeError:
   pass