# functions


def say_hello():
    print("Hello")


say_hello()


# Arguments


def say_hello(name):
    print("Hello " + name)


say_hello("Asim")
say_hello("Jose")


# return function


def add_num(num1, num2):
    return num1 + num2


sum = add_num(4, 2)
print(sum)