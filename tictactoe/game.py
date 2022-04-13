"""
game.py
Dylan Palmieri
2021-02-07
Main game functions for 5x5 Tic-Tac-Toe

This module contains the game code for the tictactoe module.

Included is the print_board method, the check_win method, and the game method.
"""


from time import localtime, strftime
import ai


def print_board(board):
    """
    This method, given a board, prints the board in the standard
    tic-tac-toe board format.
    """
    if len(board) != 25:
        print("Something's wrong with the board. len() != 25")
        return

    print()
    print()
    print("             |       |       |       |      ")
    print("         {}   |   {}   |   {}   |   {}   |   {}   ".format(
        board[0], board[1], board[2], board[3], board[4]))
    print("      _______|_______|_______|_______|_______")
    print("             |       |       |       |      ")
    print("         {}   |   {}   |   {}   |   {}   |   {}   ".format(
        board[5], board[6], board[7], board[8], board[9]))
    print("      _______|_______|_______|_______|_______")
    print("             |       |       |       |      ")
    print("         {}   |   {}   |   {}   |   {}   |   {}   ".format(
        board[10], board[11], board[12], board[13], board[14]))
    print("      _______|_______|_______|_______|_______")
    print("             |       |       |       |      ")
    print("         {}   |   {}   |   {}   |   {}   |   {}   ".format(
        board[15], board[16], board[17], board[18], board[19]))
    print("      _______|_______|_______|_______|_______")
    print("             |       |       |       |      ")
    print("         {}   |   {}   |   {}   |   {}   |   {}   ".format(
        board[20], board[21], board[22], board[23], board[24]))
    print("             |       |       |       |      ")
    print()
    print()


def check_win(board):
    """
    This function checks for all possible five-in-a-row wins on a
    5x5 tic-tac-toe board.
    """
    # Possible Horizontal Wins
    horizontal = [0, 5, 10, 15, 20]
    for i in horizontal:
        if (board[i] != ' '
           and board[i] == board[i + 1] == board[i + 2] == board[i + 3]):
            return board[i]

    # Possible Diagonal wins, left to right
    l_diagonal = [0]
    for i in l_diagonal:
        if (board[i] != ' '
           and board[i] == board[i + 5 + 1] == board[i + 10 + 2] == board[i + 15 + 3]):
            return board[i]

    # Possible Diagonal wins, right to left
    r_diagonal = [4]
    for i in r_diagonal:
        if (board[i] != ' '
           and board[i] == board[i + 5 - 1] == board[i + 10 - 2] == board[i + 15 - 3]):
            return board[i]

    # Possible Vertical wins
    for i in range(5):
        if (board[i] != ' '
           and board[i] == board[i + 5] == board[i + 10] == board[i + 15]):
            return board[i]

    # Possible draw
    draw = True
    for char in board:
        if char == ' ':
            draw = False

    if draw:
        return "draw"

    return ' '

def game(board, player, algorithm_one="", algorithm_two=""):
    """
    This function contains the main game loop for the tictactoe module.
    """
    board_list = []

    empty_board = []
    for _ in range(25):
        empty_board.append(' ')

    turn = 'X'

    if board != empty_board:
        num_x = board.count('X')
        num_o = board.count('O')

        if num_x != num_o:
            turn = 'O'

    print("Based on the state of the board, I can see that ", end="")
    print(f"it is {turn}'s turn.")

    while True:
        board_list.append(board.copy())

        print("This is the current board state:")
        print_board(board)
        print(f"It is \'{turn}\' player's move:")

        if (turn == 'O' and player == '2') or player == '3':
            if (player == '3' and turn == 'X') or player == '2':
                ai.ai_move(board, turn, algorithm_one)
            elif player == '3' and turn == 'O':
                ai.ai_move(board, turn, algorithm_two)

        else:
            print(f"Where would you like to place your \'{turn}\'?")
            print("Format your move as a number between 1 and 25, ", end="")
            print("and 25 being the bottom right.", end="")
            move = input("Please enter your move: ")

            move = int(move) - 1
            if 0 <= move <= 24 and board[move] not in ('X', 'O'):
                board[move] = turn
            else:
                print("Please enter a valid move.")
                continue

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        winner = check_win(board)
        if winner in ('X', 'O'):
            print(f"We have a winner! \'{winner}\' wins!")
            print_board(board)
        elif winner == "draw":
            print("It's a draw!")
        else:
            continue

        return
