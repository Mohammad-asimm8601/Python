# range

for num in range(2, 10, 2):
    # print even num
    print(num)


# generator
print(list(range(0, 11, 2)))


# enumerator- gives index

word = "abcde"
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print("\n")


# zip function
mylist1 = [1, 2, 3]
mylist2 = ["a", "b", "c"]
mylist3 = [100, 200, 300]

for item in zip(mylist1, mylist2, mylist3):
    print(item)

print(list(zip(mylist1, mylist2)))


# in operator

print("x" in [1, 2, 3])


# min and max function

mylist = [10, 20, 3, 40, 50, 100]
print(min(mylist))
print(max(mylist))


# import library
from random import shuffle

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(mylist)
print(mylist)


from random import randint
rand = (randint(0, 100))


# input function
num = input('Enter a number here : ')

