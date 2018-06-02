foo = "Number 1:", 12, "\nNumber 2: ", 13, "\nNumber 3: ", 13, "\nNumber 4: ", 14
bar = map(str, foo)
print(bar)
print(''.join(bar))

foo2 = "Number 1:","\nNumber 2: ","\nNumber 3: ","\nNumber 4: "
print(foo2)
print(''.join(foo2))

foo3 = ["Number 1:","\nNumber 2: ","\nNumber 3: ","\nNumber 4: "]
print(foo3)
print(''.join(foo3[2]))