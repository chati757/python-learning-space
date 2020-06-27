test_global_var = 12

def call_global_var():
    print('call in call global var')
    print(test_global_var) # 12

def edit_global_var():
    print('call in edit global var')
    #global test_global_var if not declare global it's will be local var.
    test_global_var = 14 # is local
    print(test_global_var)

if __name__ == "__main__":
    call_global_var()
    edit_global_var()
    print(test_global_var)
    pass