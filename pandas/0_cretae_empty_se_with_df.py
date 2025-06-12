def build_empty_series_with_dataframe(df_ref_dtype:pd.DataFrame):
    df_buff = df_ref_dtype.copy()
    df_buff.loc[df_buff.index[-1]+1,:] = None
    se = df_buff.iloc[-1]
    return se       

if __name__=='__main__':
    pass