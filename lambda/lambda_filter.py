number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]

#use list comprehensions instread of using lambda and filter
print([i for i in number_list if i < 0]) 