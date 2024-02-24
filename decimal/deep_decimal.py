from itertools import combinations

def deep_decimal(arr,fix_pos,left_pos,right_pos):
    #0 1 2
    #[0.96,.04,0]
    arr_buff = [round(i,2) for i in arr]
    result_buff_arr = []
    buff_sub_arr = []
    shift = 0.001
    left_val = arr_buff[left_pos]
    right_val = arr_buff[right_pos]

    if(arr_buff[fix_pos] == 0):
        #fix lower
        #ulr and url
        fix_upper = arr_buff[fix_pos]
        for i in range(1,10):
            buff_shift = round(i*shift,3)
            if(left_val>0):
                buff_sub_arr = [round(left_val-(buff_shift),3),round(right_val+(buff_shift),3)]
                buff_sub_arr.insert(fix_pos,fix_upper)
                result_buff_arr.append(buff_sub_arr)
            
            if(right_val>0):
                buff_sub_arr = [round(left_val+(buff_shift),3),round(right_val-(buff_shift),3)]
                buff_sub_arr.insert(fix_pos,fix_upper)
                result_buff_arr.append(buff_sub_arr)

    else:
        #fix pos normal
        #ulr and url
        fix_upper = round(arr_buff[fix_pos]-shift,3)
        for i in range(1,10):
            buff_shift = round(i*shift,3)
            if(left_val>0):
                buff_sub_arr = [round(left_val-(buff_shift)+shift,3),round(right_val+(buff_shift),3)]
                buff_sub_arr.insert(fix_pos,fix_upper)
                result_buff_arr.append(buff_sub_arr)

            if(right_val>0):
                buff_sub_arr = [round(left_val+(buff_shift),3),round(right_val-(buff_shift)+shift,3)]
                buff_sub_arr.insert(fix_pos,fix_upper)
                result_buff_arr.append(buff_sub_arr)

        #llr and lrl
        fix_lower = round(arr_buff[fix_pos]+shift,3)
        for i in range(1,10):
            buff_shift = round(i*shift,3)
            if(left_val>0):
                buff_sub_arr = [round(left_val-(buff_shift)-shift,3),round(right_val+(buff_shift),3)]
                buff_sub_arr.insert(fix_pos,fix_lower)
                result_buff_arr.append(buff_sub_arr)

            if(right_val>0):
                buff_sub_arr = [round(left_val+(buff_shift),3),round(right_val-(buff_shift)-shift,3)]
                buff_sub_arr.insert(fix_pos,fix_lower)
                result_buff_arr.append(buff_sub_arr)

    return result_buff_arr

if __name__=="__main__":
    test_arr = [0.97, 0.01, 0.02]#[0.96,.04,0]
    result_arr = []
    for fix_pos in range(len(test_arr)):
        arr_except_fix = list(range(len(test_arr)))
        arr_except_fix.pop(arr_except_fix.index(fix_pos))
        for left,right in combinations(arr_except_fix,2):
            result_arr.append(deep_decimal(test_arr,fix_pos,left,right))

    import pdb;pdb.set_trace()