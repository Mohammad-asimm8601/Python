from random import shuffle

# Initial list
my_list = [" ", "O", " "]

# shuffle list
shuffle(my_list)


# User guess
def player_guess():

    guess = ""
    while guess not in ["0", "1", "2"]:
        guess = input("pick a number(0,1, or 2):- ")

    return int(guess)


my_idx = player_guess()


# check guess
def check_guess(my_list, guess):
    if my_list[guess] == "O":
        print("Correct!")
    else:
        print("Wrong guess!")
        print(my_list)


check_guess(my_list, my_idx)
