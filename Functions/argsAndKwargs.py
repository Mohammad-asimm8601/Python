def myfunc(a,b):
    # Returns 5% of the sum of a and b
    return sum((a, b)) * 0.05

result = myfunc(40, 60)
print(result)


# Using *args- add using tuple

def myfunc(*args):
    return sum(args) * 0.05

result = myfunc(10, 40 ,30) 
print(result)


# **kwargs - dict

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruits here')
    
myfunc(juice = 'apple', fruit= 'orange')