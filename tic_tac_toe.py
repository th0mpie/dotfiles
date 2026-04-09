#!/usr/bin/env python3

import os

#### board is een lijst geen matrix !

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

current_player = "X"

def print_board(board):
    print("+---+---+---+")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("+---+---+---+")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("+---+---+---+")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("+---+---+---+")


while True:
    os.system('clear')
    print_board(board)

#### move maken

    move = input("choose 1-9: | q = exit ")
    if move == "q":
        break

    index = int(move) -1
    if index < 0 or index > 9:
        input("press any key to continue")
        print("Invalid input nigga")
        continue

    if board[index] != " ":
        print("Space already occupied nigga")
        input("press any key to continue")
        continue

    board[index] = current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"



    def win_condition(board, current_player): 
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]


        for a, b, c in wins:
            if board[a] == board [b] == board[c] == current_player:
                return True
            else:
                return False 
    
    if win_condition True:
        os.system('clear')
        print("{current_player} wins")
        break


