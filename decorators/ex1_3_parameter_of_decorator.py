def decorator(**parameter):
    print("Inside decorator")
    print(parameter)
    def middle(original_func):
        print("Inside inner")
        def warper(*args):
            # code functionality here
            print("Inside inner function")
            original_func(*args)
        # returning wraper function   
        return warper
    return middle
 
@decorator(dec_para="geeksforgeeks")
def my_func(func_para="no"):
    print("Inside actual function")
    print(func_para)

if __name__=="__main__":
    my_func("ok")