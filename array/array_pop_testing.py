protocal_list=['http://','https://']

try:
    print(protocal_list.pop())
    print(protocal_list.pop())
    print(protocal_list.pop())
except IndexError as e:
    print(str(e))
    if(str(e)=="pop from empty list"):
        print("ok")