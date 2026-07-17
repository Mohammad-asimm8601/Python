# while loops

pool = 'empty'
while pool == 'empty' :
    print("Keep filling my pool with water")
    break;
else:
    print("My pool is full")


x = 0
while x > 5 :
    print(f'The value of x is {x}')
    x += 1
else:
    print("x  is not less than 5")



# break, continue, pass keyword

x = [1, 2, 3]

for item in x:
    pass
print('end of my script')


mystring = 'Sammy'

for letter in mystring:
    if(letter == 'a'): continue
    print(letter)