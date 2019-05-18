WIDTH = 500

alien = Actor('alien')
alien.x = 0
alien.y = 50


def draw():
    screen.clear()
    alien.draw()


def update():
    alien.x += 2
    if alien.x > WIDTH:
        alien.x = 0

