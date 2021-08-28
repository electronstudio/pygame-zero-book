from richlib import *

cube = Cube((0, 10, 0), (10, 20, 10), 'blue')

def draw():
    clear()
    cube.draw()


def update():
    cube.pos = mouse.ground_position

    if mouse.left_button:
        print("button held down")
    if mouse.clicked:
        print("mouse click")


run()
