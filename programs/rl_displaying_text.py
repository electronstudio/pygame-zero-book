
from richlib import *

score = 0

def draw():
    clear()

def draw2d():
    screen.draw_text(f"Player 1 score: {score}", 0, 0, 20, VIOLET)

def update():
    global score
    if keyboard.key_pressed('space'):
        score += 1

run()

