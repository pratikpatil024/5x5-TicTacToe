"""
tictactoe.py
Dylan Palmieri
2021-02-07
main function for 5x5 Tic-Tac-Toe

This module contains the main UI loop for the tictactoe module.

It holds the main function.
"""


from time import sleep
from game import game
from game import print_board

def main():
    """
    The main function holds the main UI for the tictactoe module.
    """
    while True:
        board = []
        path = ""
        for _ in range(25):
            board.append(' ')

        print("\nWelcome to 5x5 Tic-Tac-Toe!")
        print("\nWould you like to play against:")
        print("[1] A human player.")
        print("[2] An AI player.")
        print("[3] I'd like to watch two AI players play.")
        print("[4] Exit the game.")
        player = input("\nPlease choose either 1, 2, 3, or 4: ")
        if player not in ('1', '2', '3', '4'):
            print("Please choose again.")
            continue

        if player == '4':
            break

        algorithm_one = ""
        algorithm_two = ""
        if player == '2' or player == '3':
            print("\nWhich algorithm would you like the AI/First AI to use?")
            print("[1] Minimax.")
            print("[2] Monte-Carlo Tree Search")
            algorithm_one = input("\nPlease choose either 1 or 2: ")
            if algorithm_one not in ('1', '2'):
                print("Please choose again.")
                continue

        if player == '3':
            print("\nWhich algorithm would you like the second AI to use?")
            print("[1] Minimax.")
            print("[2] Monte-Carlo Tree Search")
            algorithm_two = input("\nPlease choose either 1 or 2: ")
            if algorithm_two not in ('1', '2'):
                print("Please choose again.")
                continue

        algorithm_one = "minimax" if algorithm_one == '1' else "mcts"
        algorithm_two = "minimax" if algorithm_two == '1' else "mcts"

        game(board, path, player, algorithm_one, algorithm_two)

    print("\nGoodbye.")


if __name__ == '__main__':
    main()
