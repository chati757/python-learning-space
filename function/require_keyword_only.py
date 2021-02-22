def re_k(a,*,b,c):
    print(a)
    print(b)
    print(c)

if __name__ == '__main__':
    re_k(1,b=2,c=3)
    re_k(1,b=2,3) # error
    re_k(1,2,c=3) # error