import random
import math

WIDTH = 600
HEIGHT = 800

player = Actor("alien", (300, 780))
player.vx = 0   # horizontal velocity
player.vy = 1   # vertical velocity

lines = []          # list of tuples of horizontal lines of walls
wall_gradient = -3  # steepness of wall
left_wall_x = 200   # x-coordinate of wall
distance = 0        # how far player has travelled
time = 15           # time left until game ends
playing = False     # True when in game, False when on title screen
best_distance = 0   # remember the highest distance scored

def draw():
    screen.clear()
    if playing: # we are in game
        for i in range(0, len(lines)): # draw the walls
            x, x2, color = lines[i]
            screen.draw.line((0, i), (x, i), color)
            screen.draw.line((x + x2, i), (WIDTH, i), color)
        player.draw()
    else:   # we are on title screen
        screen.draw.text("PRESS SPACE TO START",
            (150, 300),color="green",fontsize=40)
        screen.draw.text("BEST DISTANCE: "+str(int(best_distance / 10)),
            (170, 400), color="green", fontsize=40)
    screen.draw.text("SPEED: " + str(int(player.vy)),
        (0, 0), color="green", fontsize=40)
    screen.draw.text("DISTANCE: " + str(int(distance / 10)),
        (200, 0), color="green", fontsize=40)
    screen.draw.text("TIME: " + str(int(time)),
        (480, 0), color="green", fontsize=40)


def update(delta):
    global playing, distance, time
    if playing:
        wall_collisions()
        scroll_walls()
        generate_lines()
        player_input()
        timer(delta)
    elif keyboard.space:
        playing = True
        distance = 0
        time = 10


def player_input():
    pass

def generate_lines():
    pass

def scroll_walls():
    pass

def wall_collisions():
    pass

def timer(delta):
    pass

def on_mouse_move(pos):
    pass
