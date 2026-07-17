str = 'hello'

my_list = []
for letter in str:
    my_list.append(letter)

print(my_list)


# list comprehensive

my_list = [letter for letter in str]
print(my_list)


my_list = [num*num for num in range(1,11)]
print(my_list)



# even list
my_list = [num for num in range(0,11) if num%2 == 0]
print(my_list)


celcius = [0, 10, 20, 34.5, 37]

fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)


results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

my_list = [x*y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(my_list)