#!/usr/bin/env python3

import curses
import random
import time

def main(stdscr):
    # --------------------------
    # Curses setup
    # --------------------------
    curses.curs_set(0)            # verberg cursor
    stdscr.nodelay(True)           # input non-blocking
    stdscr.timeout(200)            # refresh elke 200ms
    curses.use_default_colors()    # default terminal colors
    curses.init_pair(1, curses.COLOR_GREEN, -1)  # Snake = groen
    curses.init_pair(2, curses.COLOR_RED, -1)    # Food = rood

    # --------------------------
    # Grid setup
    # --------------------------
    width = 20
    height = 20

    # --------------------------
    # Snake setup
    # --------------------------
    snake = [(5, 7), (4, 7), (3, 7)]  # lijst van (x,y), kop = index 0
    direction = "RIGHT"                # startrichting

    # --------------------------
    # Food setup
    # --------------------------
    food = (random.randint(0, width - 1), random.randint(0, height - 1))

    # --------------------------
    # Score & highscore
    # --------------------------
    score = 0
    try:
        with open("highscore_snake.txt", "r") as file:
            highscore = int(file.read())
    except FileNotFoundError:
        highscore = 0

    # --------------------------
    # Flag voor game over
    # --------------------------
    game_over = False

    # --------------------------
    # Game loop
    # --------------------------
    while True:
        # Input
        key = stdscr.getch()
        if key == ord('a'):
            break
        elif key == ord('z'):
            direction = "UP"
        elif key == ord('s'):
            direction = "DOWN"
        elif key == ord('q'):
            direction = "LEFT"
        elif key == ord('d'):
            direction = "RIGHT"

        # Huidige koppositie
        head_x, head_y = snake[0]

        # Beweging
        if direction == "UP":
            head_y -= 1
        elif direction == "DOWN":
            head_y += 1
        elif direction == "LEFT":
            head_x -= 1
        elif direction == "RIGHT":
            head_x += 1

        # Wrap-around
        head_x %= width
        head_y %= height

        new_head = (head_x, head_y)
        snake.insert(0, new_head)

        # Self-collision check
        if new_head in snake[1:]:
            game_over = True
            break  # verlaat de loop onmiddellijk

        # Food check → groei
        if new_head == food:
            score += 1
            while True:
                food = (random.randint(0, width - 1), random.randint(0, height - 1))
                if food not in snake:
                    break
        else:
            snake.pop()  # verwijder staart → snake blijft even lang

        # Grid tekenen
        stdscr.clear()
        try:
            stdscr.addstr(0, 0, f"Score: {score}")
            for y in range(height):
                for x in range(width):
                    if (x, y) in snake:
                        stdscr.addstr(y + 1, x*2, "O", curses.color_pair(1))  # Snake groen
                    elif (x, y) == food:
                        stdscr.addstr(y + 1, x*2, "*", curses.color_pair(2))  # Food rood
                    else:
                        stdscr.addstr(y + 1, x*2, ".")                       # lege cel
            stdscr.addstr(height + 2, 0, "Controls: z/q/s/d = move | a = quit")
        except curses.error:
            # Terminal might be too small — ignore drawing errors
            pass
        stdscr.refresh()

    # --------------------------
    # GAME OVER scherm
    # --------------------------
    if game_over:
        stdscr.timeout(-1)     # blocking input
        curses.flushinp()      # <-- clear any leftover keypresses so getch() waits for the next key
        stdscr.clear()
        stdscr.addstr(0, 0, "GAME OVER!")
        if score > highscore:
            highscore = score
            with open("highscore_snake.txt", "w") as file:
                file.write(str(highscore))
            stdscr.addstr(1, 0, f"NEW HIGH SCORE: {highscore}")
        else:
            stdscr.addstr(1, 0, f"Final score: {score} | High score: {highscore}")
        stdscr.addstr(3, 0, "Press any key to exit")
        stdscr.refresh()
        stdscr.getch()  # wacht op toets, pas daarna return

# --------------------------
# Start de game
# --------------------------
if __name__ == "__main__":
    curses.wrapper(main)
