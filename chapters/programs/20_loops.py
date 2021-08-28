WIDTH = 500
HEIGHT = 500

def draw():
    screen.clear()
    for x in range(0, WIDTH, 40):
        screen.draw.filled_circle((x, 20), 20, "red")

    for x in range(0, WIDTH, 40):
        for y in range(60, HEIGHT, 40):
            screen.draw.filled_circle((x, y), 10, "green")
