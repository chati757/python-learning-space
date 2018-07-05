from functools import partial

def calculate(a,b,c):
    return 2*a+3*b+4*c

A=calculate
B=A(1,2,3)

C=partial(calculate,1,2)
D=C(3)

print(C)
print(D)