# wiggle your mouse around the screen!

alien = Actor("alien")

def draw():
    screen.clear()
    alien.draw()

def on_mouse_move(pos):
    alien.pos = pos

