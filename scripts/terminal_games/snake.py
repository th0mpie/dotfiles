#!/usr/bin/python3

import curses
import time
import random
import os

def main(stdscr):
    curses.curs_set(0)  # verberg cursor
    stdscr.nodelay(True) # input non-blocking
    stdscr.timeout(200)  # refresh elke 200ms

    width = 10
    height = 10
    
    snake_x = width // 2
    snake_y = height // 2
    snake = [(snake_x, snake_y)]
 
    direction = "right"
    
    food_x = random.randint(0, width-1)
    food_y = random.randint(0, height-1)
    
    score = 0

    while True:
        # lees key
        key = stdscr.getch()
        if key == ord('z'): direction = "up"
        elif key == ord('s'): direction = "down"
        elif key == ord('q'): direction = "left"
        elif key == ord('d'): direction = "right"

        # snake verplaatsen
        if direction == "up": snake_y -= 1
        elif direction == "down": snake_y += 1
        elif direction == "left": snake_x -= 1
        elif direction == "right": snake_x += 1

        # wrap-around
        snake_x %= width
        snake_y %= height

        # food check
        if (snake_x, snake_y) == (food_x, food_y):
            score += 1
            while True:
                food_x = random.randint(0, width-1)
                food_y = random.randint(0, height-1)
                if (food_x, food_y) != (snake_x, snake_y):
                    break

        # grid tekenen
        stdscr.clear()
        stdscr.addstr(0,0,f"Score: {score}")
        for y in range(height):
            line = ""
            for x in range(width):
                if x == snake_x and y == snake_y:
                    line += "O"
                elif x == food_x and y == food_y:
                    line += "*"
                else:
                    line += "."
            stdscr.addstr(y+1,0,line)
        stdscr.refresh()
        time.sleep(0.2)

curses.wrapper(main)

