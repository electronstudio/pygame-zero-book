alien = Actor('alien')
alien.pos = (0, 50)


def draw():
    screen.clear()
    alien.draw()


def update():
    if (keyboard.right):
        alien.x = alien.x + 2
    elif (keyboard.left):
        alien.x = alien.x - 2

