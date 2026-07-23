# Hello there! First off, make sure you understand the project scope. what needs to happen?

# 1) Greet the players and ask his names
# 2) We need to print a board
# 3) Take in player input
# 4) Place their input on the board
# 5) Check if the game is won, tied, lost, or ongoing
# 6) Repeat 4 and 5 until hte game has been won or tied
# 7) Ask if players want to play again


# greet

def game_greet():
    print('\n')

    title = "<---- Welcome  To  Tic  Tac  Toe  Game ---->"
    divider = "=" * len(title)

    print("\t"+divider)
    print("\t"+title.upper())  
    print("\t"+divider)

    print('\n')


# Display board

def display_board(board):

    print("\t\t  | " + "  | ")
    print("\t\t"+board[1] + " | " + board[2] + " | " + board[3])
    print("\t\t  | " + "  | ")
    print("\t\t----------")
    print("\t\t  | " + "  | ")
    print("\t\t"+board[4] + " | " + board[5] + " | " + board[6])
    print("\t\t  | " + "  | ")
    print("\t\t----------")
    print("\t\t  | " + "  | ")
    print("\t\t"+board[7] + " | " + board[8] + " | " + board[9])
    print("\t\t  | " + "  | ")
    print('\n')



# player input


def player_input():
    marker = ""

    # keeping asking player 1 too choose X or O

    while marker != "X" and marker != "O":
        marker = input("Player 1, choose X or O: ")

    # Assign player 2, the opposite marker
    player1 = marker

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return (player1, player2)


# Take Person name

def person_name():

    player1 = "123"
    player2 = "123"


    while player1.isdigit() == True:

        player1 = input("Player 1, Enter your name: ")
        if player1.isdigit() == True:
            print("Sorry, that is not a name!")


    player1_maker, player2_maker = player_input(player1)

    
    while player2.isdigit() == True:

        player2 = input("Person 2, Enter your name: ")

        if player2.isdigit() == True:
            print("Sorry, that is not a name!")
    print('\n')


    print(f'Hello {player1} and {player2}. I am pleased to welcome you')
    print('\n')

# main part (calling function)

def main():

    test_board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    test_board[1] = 'X'
    game_greet()
    person_name()
    display_board(test_board)

main() 
