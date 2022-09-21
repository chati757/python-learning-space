import pandas as pd

def check_global(var):
    result=None
    try:
        if(isinstance(var,pd.DataFrame)==True):
            result = [key for key,val in globals().items() if(id(val)==id(var))][0]
        else:
            result = [key for key,val in globals().items() if(val==var)][0]
    except IndexError:
        pass
    return result!=None


if __name__=="__main__":
    print('checking global variable')
    global global_x
    global_x = 2

    '''
    ไม่สามารถตรวจว่าเป็น global variable หรือไม่จาก value ไม่ได้
    '''
    print(check_global(global_x))#global_x
    global_x2 = 2
    print(check_global(global_x2))#global_x
    
    '''
    สามารถตรวจว่าเป็น global variable หรือไม่จาก value ได้
    '''
    print('checking global_df')
    global global_df
    global_df = pd.DataFrame({'a':[2,3,4]})
    print(check_global(global_df))#global_df

    print('checking global_dict')
    global global_dict
    global_dict = {'testkey':'testval'}
    print(check_global(global_dict))

    print('checking global_list')
    global global_list
    global_list = ['test']