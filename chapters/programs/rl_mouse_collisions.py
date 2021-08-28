from richlib import *

cube = Cube((0, 10, 0), (10, 20, 10), 'blue')

def draw():
    clear()
    cube.draw()


def update():
    cube.x = cube.x + 1
    if cube.x > 100:
        cube.x = -100
    if mouse.clicked:
        if mouse.check_collision(cube):
            print("hit")
        else:
            print("miss")

run()
