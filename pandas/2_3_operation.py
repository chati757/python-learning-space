import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())

#----------------------------- counting ----------------------------
'''
col1  col2 col3
0     1   444  abc
1     2   555  def
2     3   666  ghi
3     4   444  xyz
'''

print(df['col2'].unique())
'''
[444 555 666]
'''

print(df['col2'].nunique())
'''
3
'''

print(df['col2'].value_counts())
'''
444    2
555    1
666    1
Name: col2, dtype: int64
'''
#-------------------------------------------------------------------
#------------------------apply function-----------------------------
def times_two(number):
    return number * 2

df['new'] = df['col1'].apply(times_two)
# or df['new'] = df['col1'].apply(lambda number:number * 2)
print(df)
'''
col1  col2 col3  new
0     1   444  abc    2
1     2   555  def    4
2     3   666  ghi    6
3     4   444  xyz    8
'''
#-------------------------------------------------------------------
