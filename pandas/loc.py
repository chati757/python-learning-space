df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],index=['cobra', 'viper', 'sidewinder'],columns=['max_speed', 'shield'])

df.loc[df['shield'] > 3]
print(df)
'''
max_speed  shield
viper               4       5
sidewinder          7       8
'''

df.loc[df['shield'] > 3] = 0
print(df)
'''
max_speed  shield
cobra               1       2
viper               0       0
sidewinder          0       0
'''

df.loc[df['shield'] > 3,'shield'] = 0
print(df)
'''
            max_speed  shield
cobra               1       2
viper               4       0
sidewinder          7       0
'''

df.loc[:,'new_column'] = pd.Series([None],dtype='float64')
'''
#create new column and empty all rows and specify type to float64
            max_speed  shield  new_column
cobra               1       2         NaN
viper               0       0         NaN
sidewinder          0       0         NaN
'''

