#!/usr/bin/env python3

import random
import os

coin = ["heads", "tails"]
play_again = "y"

while play_again == "y":
    os.system('clear')

# input validatie
    while True:
        user_input = input("==== Press Enter To Flip ====")
        if user_input == "":
            break
        else: 
            print("Don't mess with the coin!")

    result = random.choice(coin)
    print(f"It's {result}!")

    play_again = input("Flip again? (y/n): ").lower()
    
