import pandas as pd

df = pd.DataFrame({'a':[1,2,3],'b':[5,6,7]})

df.somemeta = 'testmeta'

print(df.somemeta)