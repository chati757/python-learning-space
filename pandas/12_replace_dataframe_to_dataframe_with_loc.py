test_df1 = pd.DataFrame({'a':[1,2,3,4],'b':[4,-1,-1,7]}) #สมมุติว่า เลข -1 คือเลขที่ควรแก้ไข เป็น 5 และ 6 ตาม test_df2
'''
   a  b
0  1  4
1  2 -1
2  3 -1
3  4  7
'''
test_df2 = pd.DataFrame({'a':[2,3],'b':[5,6]}) #คือข้อมูลที่ถูกต้อง
'''
   a  b
0  2  5
1  3  6
'''
test_df_merge = test_df1.merge(test_df2,on=['a'])
test_df_merge.drop([i for i in test_df_merge if i.endswith('_x')],axis=1,inplace=True)
#test_df_merge.columns = map(lambda x:x.replace('_y','') if(x.endswith('_y')) else x,test_df_merge.columns)
test_df_merge.columns = [i if not i.endswith('_y') else i.replace('_y','') for i in test_df_merge.columns]
test_df_con = pd.concat([test_df1,test_df_merge],sort=False,ignore_index=True).drop_duplicates(subset='a',keep='last').sort_values(by='a')
'''
   a  b
0  1  4
4  2  5
5  3  6
3  4  7
'''
try:
    test_df_con.index = test_df1.index
except ValueError:
    #df.index = np.arange(1,len(df)+1)
    test_df_con.index = np.arange(test_df1.index[0],test_df1.shape[0])

'''
   a  b
0  1  4
1  2  5
2  3  6
3  4  7
'''
'''
#drop old data (old columns it's end with _x)
df_buff.drop([i for i in df_buff.columns if i.endswith('_x')],axis=1,inplace=True)
#change columns if end with _y change to '' Ex.High_y , Low_y , Close_y , Open_y --> High , Low , Close , Open
df_buff.columns = map(lambda x:x.replace('_y','') if(x.endswith('_y')) else x,df_buff.columns)
#concat std_df ,drop_duplicate , sort by date , reset_index
pd.concat([std_df,df_buff],sort=False,ignore_index=True).drop_duplicates(subset='Date',keep='last').sort_values(by='Date').reset_index(drop=True)
'''