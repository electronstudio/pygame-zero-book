
from richlib import *
import random
import time

TIME = 20
NUMBER_OF_BALLS = 10
JUMP_POWER = 2

start_time = time.time()
time_left = TIME

CAMERA = screen.CAMERA_FIRST_PERSON

balls = []
for i in range(0, NUMBER_OF_BALLS):
    ball = Sphere()
    ball.x = random.randint(-300, 300)
    ball.y = random.randint(10, 40)
    ball.z = random.randint(-300, 0)
    ball.color = 'green'
    balls.append(ball)

score = 0

alien = Actor('trooper')
alien.size = (10, 10, 10)
alien.collision_radius = 5

alien.yv = 0
alien.xv = 0
alien.zv = 0

sound = Sound('eep')
sound.volume = 0.7
sound.pitch = 0.5


def draw():
    clear()
    alien.draw()
    for ball in balls:
        ball.draw()


def draw2d():
    if (time_left > 0):
        screen.draw_text(f"Score: {score}       Time: {time_left}", 0, 0, 50, VIOLET)
    else:
        screen.draw_text(f"Your Score: {score}\nOUT OF TIME", 30, 50, 50, RED)


def update():
    global score
    global time_left

    time_left = int(TIME + (start_time - time.time()))
    if time_left <= 0:
        return

    alien.yv -= 0.05

    alien.x += alien.xv
    alien.y += alien.yv
    alien.z += alien.zv

    if alien.y <= 0:  # Only control when alien is on ground
        if keyboard.right:
            alien.xv += 0.1
        elif keyboard.left:
            alien.xv -= 0.1
        if keyboard.down:
            alien.zv += 0.1
        elif keyboard.up:
            alien.zv -= 0.1

        if keyboard.space:
            alien.yv = JUMP_POWER

        if alien.xv > 0.05:
            alien.xv -= 0.05
        elif alien.xv < -0.05:
            alien.xv += 0.05

        if alien.zv > 0.05:
            alien.zv -= 0.05
        elif alien.zv < -0.05:
            alien.zv += 0.05

        alien.y = 0

    for ball in balls:
        if alien.check_collision(ball):
            balls.remove(ball)
            sound.play()
            score += 1


run()
