#!/usr/bin/env python3

import random
import os

choices = ["rock", "paper", "scissors"]
play_again = "y"
player_score = 0
computer_score = 0

while play_again.lower() == "y":
    os.system('clear')

    print("========================")
    print("Rock – Paper – Scissors")
    print("========================")
    print()
    print("Choose an option:")
    print("------------------------")
    print("1) Rock")
    print("2) Paper")
    print("3) Scissors")
    print("------------------------")

    # input-validatie loop
    while True:
        user_input = input("Type the number of your choice: ")
        if user_input in ["1", "2", "3"]:
            player = choices[int(user_input) - 1]
            break
        else:
            print("Invalid input. Please try again.\n")

    os.system('clear')
    computer = random.choice(choices)
    print("----------------------------------------")
    print(f"Player: {player} | Computer: {computer}")
    print("----------------------------------------")

    if player == computer:
        print("It's a tie!")
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print("----------------------------------------")
    print(f"Player: {player_score}  |  Computer: {computer_score}")
    print("----------------------------------------")


    while True:
        play_again = input("Try again? (y/n): ").lower()
        if play_again in ["y", "n"]:
            break
        else:
            print("Invalid input. Please type 'y' or 'n'.")
