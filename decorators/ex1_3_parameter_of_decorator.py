def decorator(**parameter):
    print("Inside decorator")
    print(parameter)
    def middle(original_func):
        print("Inside inner")
        def warper(*args):
            # code functionality here
            print("Inside inner function")
            print("I like", args['like'])
            original_func()
        # returning wraper function   
        return warper
    return middle
 
@decorator(test="geeksforgeeks")
def my_func():
    print("Inside actual function")