
my_nums = [10,21, 32, 43, 54]
print(list(map(lambda num : num**2, my_nums)))

print(list(filter(lambda num : num%2 == 0, my_nums)))
