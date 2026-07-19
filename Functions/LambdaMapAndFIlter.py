# map


def square(num):
    return num**2


my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item, end=" ")
print("\n")

print(list(map(square, my_nums)))


# filter

def check_even(num):
    return num % 2 == 0

num_list = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(list(filter(check_even, num_list)))


# lambda

square = lambda num : num**2
print(square(3))


my_nums = [10,21, 32, 43, 54]
print(list(map(lambda num : num**2, my_nums)))

print(list(filter(lambda num : num%2 == 0, my_nums)))
