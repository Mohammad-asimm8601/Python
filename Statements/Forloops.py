# for loops

my_iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for item_name in my_iterable:
    print(item_name)

for num in my_iterable:
    # check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd NUmber : {num}")

list_sum = 0
for num in my_iterable:
    list_sum += num
print(list_sum)


mystring = "Hello World"
for letter in mystring:
    print(letter, end=" ")


tuple = (1, 2, 3, 4)
for item in tuple:
    print(item, end=" ")
print("\n")


my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
for item in my_list:
    print(item)


for a, b in my_list:
    print(a)
    print(b)


d = {"k1": 1, "k2": 2}
for key, value in d.items():
    print(key, value)
