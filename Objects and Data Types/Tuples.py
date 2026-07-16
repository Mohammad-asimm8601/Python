# Tuples are very similar to lists. however they have one key difference- immutability. Once an element is inside a tuple, it can not be reassigned.

t = (1, 2, 3)
print(t)
print(type(t))

t = ("a", "a", "b")
print(t)
print(len(t))
print(t.count("a"))

print(t.index("a"))
