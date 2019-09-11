from richlib import *

WIDTH = 500
HEIGHT = 500

cube1 = Cube((25, 0, 0))
cube2 = Cube((-25, 0, 0))
sphere = Sphere((0, 0, 0))

cube1.color = (150, 0, 0)
cube2.color = BLUE


def draw():
    clear()
    cube1.draw()
    cube2.draw()
    sphere.draw()


run()
