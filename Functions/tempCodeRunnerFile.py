
def myfunc(kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruits here')
    
myfunc(juice = 'apple', fruit= 'orange')