# Tic-Tac-Toe


import random


def is_board_full(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return False
    return True

"""
is_board_full(board) function is used to check whether all the 9 elements are filled up or not.

After an element is inserted we check whether the matrix is completely filled up or not to declare that game is 'draw' if it is filled up.
"""



def print_board(board):
    print(board[0][0] + '|' + board[0][1] + '|' + board[0][2])
    print('-+-+-') 
    print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
    print('-+-+-')
    print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])
    
"""
print_board(board) function is used to print the 3x3 matrix after filling each element with either 'X' or 'O'.
 
We will use this function in each iteration i.e., after inserting 'X' or 'O' into the matrix we will print the entire 3x3 matrix to show at which position the player has inserted on his turn.
 
The print('-+-+-') is used to visually differentiate between each row.
"""



def is_winner(board, player):
    # check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

"""
is_winner(board, player) function is used to predict the winner by checking any row or column or diagonals of a 3x3 matrix is filled with either 'X' or 'O' completely.
 
After a player inserts his element on his turn, this function will go through each row, column and diagonally to check if it is filled with three same elements.
 
If any of the row or column or a diagonal is filled with the same element, then we declare that player wins.
"""



def play():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player = random.choice(['X', 'O'])
    print("Current player: " + player)
    while True:
        print_board(board)
        row = int(input("Enter row number between 0-2: "))  
        col = int(input("Enter column number between 0-2: "))
        if board[row][col] != ' ':
            print("Illegal move, try again.")
            continue
        board[row][col] = player
        if is_winner(board, player):
            print_board(board)
            print("Congratulations! Player " + player + " wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        player = 'X' if player == 'O' else 'O'
        print('')
        print("Current player: " + player)
    print('Do you want to play another game?')
    if input() == 'yes':
        play()
    else:
        print('GAME OVER!')
        
"""

The play() function is used to enter elements into the matrix by taking inputs from the players. The program executes as follows: 
--> We intialize an empty 3x3 matrix 'board' with all the elements keeping empty.

--> First it choses which player plays first with the help of random function so that the program is not biased towards any player.

--> After chosing the player, it prints who is playing this turn. 

--> The while loop is used to iterate the game until it gets draw or a player wins.

--> We first print the empty board and asks the current player to enter row and column number in which he wants to inserts his symbol.

--> After selecting the position, we then check if the position is already taken and returns as 'illegal move' if selected. If the position is empty we assign the symbol to that position. 

--> We then check if any of the entire row or column or diagonals has same value to predict the winner. If that is the case, we declare the current player as winner and stops the game. 

--> If anyone doesn't win then we check if the board is full using is_board_full() function. If it is full, we then print that the game is a draw and stop the game.

--> If the board is not full we then change the player from the current one and go through the loop again to continue the game.

--> After a player wins or the game ends with draw, it asks whether the player want to play another game or not. If he wants to play, then he inputs as yes to restart the game or else it will print as 'GAME OVER!' and exits the function.

"""


play()

# Now we call the function play() to start the game.


