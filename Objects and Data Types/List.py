# Lists are ordered sequences that can hold a variety of objects types. It is mutable.

mylist = [1, 2, 3]
print(mylist)

mylist = ["Hola", 12, 3.24]
print(mylist)

print(mylist[0])
print(mylist[1:])


# concatenation

another_list = ["Apple", "cherry", "grapes"]
mylist = mylist + another_list
print(mylist)

# Indexing
mylist[0] = "ONE ALL CAPS"
print(mylist)


# Append
mylist.append("Asim")
print(mylist)


# pop
print(mylist.pop())
print(mylist)

print(mylist.pop(0))
print(mylist)

# sort

new_list = ["a", "e", "x", "b", "c"]
num_list = [4, 3, 6, 2, 1, 5]

new_list.sort()
num_list.sort()

print(new_list)
print(num_list)

# reverse
num_list.reverse()
print(num_list)

print(type([42, "hello", 23.32]))
