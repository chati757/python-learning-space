import pandas as pd

df = pd.DataFrame({'a':[1,2,3,4],'b':[7,8,8,9]})

print(df['a'].isin(['3']).any())

print(3 in df['a'].values)

print(3 in df['a'].tolist())