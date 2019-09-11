from richlib import *
alien = Actor('trooper')
alien.size = (20,20,20)
alien.pos = (0, 10, 10)

def draw():
    clear()
    alien.draw()

def update():
    if keyboard.right:
        alien.x = alien.x + 1
    elif keyboard.left:
        alien.x = alien.x - 1

run()
