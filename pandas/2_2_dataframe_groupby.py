import pandas as pd

data = {
    'company':['goog','goog','msft','msft','fb','fb'],
    'person':['sam','charlie','amy','vanessa','carl','sarah'],
    'sales':[200,120,340,124,243,350]
    }

df = pd.DataFrame(data)
print(df)

'''
company   person  sales
0    goog      sam    200
1    goog  charlie    120
2    msft      amy    340
3    msft  vanessa    124
4      fb     carl    243
5      fb    sarah    350
'''

print(df.groupby('company').sum())

'''
# sales is columns
# company is name of index
        sales
company
fb         593
goog       320
msft       464
'''

print(df.groupby('company').sum().transpose())

'''
company   fb  goog  msft
sales    593   320   464
'''

#sort sales values
print(df.sort_values('sales'))

'''
company   person  sales
1    goog  charlie    120
3    msft  vanessa    124
0    goog      sam    200
4      fb     carl    243
2    msft      amy    340
5      fb    sarah    350
'''

print(df.sort_values('sales',ascending=False))

'''
company   person  sales
5      fb    sarah    350
2    msft      amy    340
4      fb     carl    243
0    goog      sam    200
3    msft  vanessa    124
1    goog  charlie    120
'''