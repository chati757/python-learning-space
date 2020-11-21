class MyNumbers:
    def __init__(self):
    print("init")

def __iter__(self):
    print("iter")
    self.a = 1
    return self

def __next__(self):
    print("next")
    if self.a <= 20:
        x = self.a
        self.a += 1
        return x
    else:
        print("end")
        raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)
print("toloop")
for x in myiter:
    print(x)
    print("endloop")