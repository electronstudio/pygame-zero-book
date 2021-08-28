WIDTH = 500
HEIGHT = 500

box = Rect((20, 20), (50, 50))

def draw():
    screen.clear()
    screen.draw.filled_rect(box, "red")


def update():
    box.x = box.x + 2
    if box.x > WIDTH:
        box.x = 0

