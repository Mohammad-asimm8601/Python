# Display

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
row2[1] = 'X'
display(row1, row2, row3)


# Accepting user input

result = int(input('Enter value:'))
print(result)
print(type(result))


position_index = int(input("chose an index position : "))
row1[position_index] = 'X'
print(row1)


# Validating user input
def user_choice():
    choice = 'WRONG'
    while choice.isdigit() == False:
        choice = input("Please enter a number (0-10): ")

        if choice.isdigit() == False:
            print("Sorry that is not a digit!")

    return int(choice)

result = user_choice()
print(result)