# IMPORTANT: switch Mu mode to "Pygame Zero" or
# nothing will appear!

WIDTH = 500
HEIGHT = 500  # what are these units?

def draw():
    screen.clear()
    screen.draw.circle((250, 250), 50, "white")
    screen.draw.filled_circle((250, 100), 50, "red")
    screen.draw.line((150, 20), (150, 450), "purple")
    screen.draw.line((150, 20), (350, 20), "purple")
