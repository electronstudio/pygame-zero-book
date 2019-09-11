from richlib import *

alien = Actor('trooper')
alien.size = (20,20,20)


def draw():
    clear()
    alien.draw()


def update():
    alien.x += 1
    if alien.x > 100:
        alien.x = -100

run()
