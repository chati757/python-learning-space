import pandas as pd

def append_dataframe_and_except_columns_to_csv(csv_path:str=None,dataframe_dict:dict=None,replace_col:bool=False):
    if(len(dataframe_dict.keys())==0):
        #receive dataframe_dict : empty
        return
    
    if(csv_path==None or (isinstance(dataframe_dict,dict) and isinstance(dataframe_dict,pd.DataFrame))):
        raise ValueError(f'append_and_except_columns_to_csv : error : csv_path==None or (isinstance(dataframe_dict,dict) and isinstance(dataframe_dict,pd.DataFrame))')
    
    if(replace_col==False):
        none_rows = [np.nan]*(len(dataframe_dict[list(dataframe_dict.keys())[0]]))
        dest_df_columns = pd.read_csv(csv_path,index_col=False,nrows=0).columns

        if(isinstance(dataframe_dict,dict)):
            if(not any([i in dest_df_columns for i in dataframe_dict.keys()])):
                return

            for col in set(dest_df_columns) - set(dataframe_dict.keys()):
                dataframe_dict[col] = none_rows
            
            dataframe_dict = {key:dataframe_dict[key] for key in dest_df_columns}

        elif(isinstance(dataframe_dict,pd.DataFrame)):
            if(not any([i in dest_df_columns for i in dataframe_dict.columns])):
                return
            
            for col in set(dest_df_columns) - set(dataframe_dict.columns):
                dataframe_dict[col] = none_rows

            dataframe_dict = {key:dataframe_dict[key].to_list() for key in dest_df_columns}

        result_df = pd.DataFrame(dataframe_dict).astype(str).replace("nan", "")
        result_df.to_csv(csv_path,mode='a',header=False,index=False,na_rep="")

    else:
        dest_df = pd.read_csv(csv_path,index_col=False)
        if(isinstance(dataframe_dict,dict)):
            df_or_se = pd.Series(dataframe_dict)
        elif(isinstance(dataframe_dict,pd.DataFrame)):
            df_or_se = dataframe_dict

        result_df = pd.concat([dest_df,df_or_se],ignore_index=True).astype(str).replace("nan", "")
        result_df.to_csv(csv_path,index=False,na_rep="")

#pd.DataFrame({'a':[9],'b':[None],'c':[9]}).to_csv('./test.csv',header=False,mode='a',index=False)
append_dataframe_and_except_columns_to_csv('./test.csv',pd.DataFrame({'a':[33,44],'b':[33,44]}),replace_col=True)


#import pdb;pdb.set_trace()