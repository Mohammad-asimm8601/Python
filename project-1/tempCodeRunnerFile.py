
def player_input():
    marker = ''

    # keeping asking player 1 too choose X or O

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')

    # Assign player 2, the opposite marker
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return (player1, player2)

player1_marker, player2_marker = player_input()
print('Player 1 : '+player1_marker)
print('Player 2 : '+player2_marker)