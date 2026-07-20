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

    # VARIABLES

    # Initial
    choice = 'WRONG'
    acceptable_range = range(0,11)
    within_range = False

    # To conditions to check
    # digit or within range == false
    while choice.isdigit() == False or within_range == False:


        choice = input("Please enter a number (0-10): ")

        # digit check
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")

        # range check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Sorry, you are  out of acceptable range!')
                within_range = False

    return int(choice)

result = user_choice()
print(result)


# simple User Interaction

# 1) Display game
game_list = [0, 1, 2]

def display_game(game_list):
    print("Here is the current list")
    print(game_list)

# display_game(game_list)

 
# 2) position choice

def position_choice():

    choice = 'wrong'

    while choice not in ['0', '1', '2']:

        choice = input("Pick a position (0,1,2): ")

        if choice not in ['0', '1', '2']:
            print("Sorry, Invalid choice! ")

    return int(choice)

# position_choice()


# Replacement choice

def replacement_choice(game_list, position):

    user_placement = input("Type a string to place at position: ")

    game_list[position] = user_placement

    return game_list

# Game On Choice

def gameon_choice():

    choice = 'wrong'

    while choice not in ['Y', 'N']:

        choice = input("Keep playing? (Y or N): ")

        if choice not in ['Y', 'N']:
            print("Sorry, I dont understand, please choose Y or N")

    if choice == "Y":
        return True
    else:
        return False
    

game_on = True
game_list = [0, 1, 2]
print('\n')
print("<---- Welcome To The Tic Tac Toe Game! ---->")
print('\n')
while game_on:

    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    display_game(game_list)

    game_on = gameon_choice()
