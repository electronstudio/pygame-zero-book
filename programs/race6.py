import random
import math

WIDTH = 600
HEIGHT = 800

player = Actor("alien", (300, 780))
player.vx = 0
player.vy = 1

lines = []
wall_gradient = -3
left_wall_x = 200
distance = 0
time = 15
playing = False
best_distance = 0

def draw():
    screen.clear()
    if playing:
        for i in range(0, len(lines)):
            x, x2, color = lines[i]
            screen.draw.line((0, i), (x, i), color)
            screen.draw.line((x + x2, i), (WIDTH, i), color)
        player.draw()
    else:
        screen.draw.text("PRESS SPACE TO START", (150, 300), color="green", fontsize=40)
        screen.draw.text("BEST DISTANCE: "+str(int(best_distance / 10)), (170, 400), color="green", fontsize=40)
    screen.draw.text("SPEED: " + str(int(player.vy)), (0, 0), color="green", fontsize=40)
    screen.draw.text("DISTANCE: " + str(int(distance / 10)), (200, 0), color="green", fontsize=40)
    screen.draw.text("TIME: " + str(int(time)), (480, 0), color="green", fontsize=40)


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
    if keyboard.up:
        player.vy += 0.1
    if keyboard.down:
        player.vy -= 0.1
        if player.vy < 1:
            player.vy = 1
    if keyboard.right:
        player.vx += 0.4
    if keyboard.left:
        player.vx -= 0.4
    player.x += player.vx


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
