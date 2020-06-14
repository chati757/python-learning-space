import pandas as pd

test_df1 = pd.DataFrame({'a':[1,2,3,4,5],'b':[4,-1,-1,7,-1]},index=[1,2,3,4,5])
'''
   a  b 
1  1  4 
2  2 -1 
3  3 -1 
4  4  7 
5  5 -1
'''
test_df2 = pd.DataFrame({'a':[2,3,4,5],'b':[5,6,7,8]})
'''
   a  b
0  2  5
1  3  6
2  4  7
3  5  8
'''
test_df_merge = pd.merge(test_df1,test_df2,on=['a'])
'''
   a  b_x  b_y
0  2   -1    5
1  3   -1    6
2  4    7    7
3  5   -1    8
'''
test_df_merge.loc[test_df_merge['b_x']!=test_df_merge['b_y'],'b_x'] = test_df_merge.loc[test_df_merge['b_x']!=test_df_merge['b_y'],'b_y']
'''
   a  b_x  b_y
0  2    5    5
1  3    6    6
2  4    7    7
3  5    8    8
'''
test_df_merge.drop([i for i in test_df_merge.columns if i.endswith('_y')],axis=1,inplace=True)
test_df_merge.columns = [i.replace('_x','') if(i.endswith('_x')) else i for i in test_df_merge.columns]
'''
   a  b
0  2  5
1  3  6
2  4  7
3  5  8
'''
test_df_con = pd.concat([test_df1,test_df_merge],sort=False,ignore_index=True).drop_duplicates(subset='a',keep='last').sort_values(by='a')
'''
   a  b 
0  1  4 
5  2  5 
6  3  6 
7  4  7 
8  5  8 
'''
try:
    test_df_con.index = test_df1.index
except ValueError:
    #df.index = np.arange(1,len(df)+1)
    test_df_con.index = np.arange(test_df1.index[0],test_df1.shape[0])

print(test_df_con)
'''
   a  b
1  1  4
2  2  5
3  3  6
4  4  7
5  5  8
'''
