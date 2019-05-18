alien = Actor("alien")
alien.pos = (0, 50)
score = 0

def draw():
    screen.clear()
    alien.draw()
    screen.draw.text("Score "+str(score), (0,0))

def update():
    if keyboard.right:
        alien.x = alien.x + 2
    elif keyboard.left:
        alien.x = alien.x - 2
    alien.image = 'alien'

def on_mouse_down(pos, button):
    global score
    if button == mouse.LEFT and alien.collidepoint(pos):
        alien.image = 'alien_hurt'
        sounds.eep.play()
        score = score + 1


