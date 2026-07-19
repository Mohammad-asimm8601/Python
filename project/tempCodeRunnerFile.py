
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