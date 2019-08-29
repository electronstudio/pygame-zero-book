WIDTH = 500
HEIGHT = 500
alien = Actor("alien")
alien.pos = (0, 50)
box = Rect((20, 20), (100, 100))

def draw():
    screen.clear()
    screen.draw.filled_rect(box, "red")
    alien.draw()
def update():
    if keyboard.right:
        alien.x = alien.x + 2
    elif keyboard.left:
        alien.x = alien.x - 2
    box.x = box.x + 2
    if box.x > WIDTH:
        box.x = 0
# PLAY SOUND AND SHOW IMAGE WHEN HIT
    if alien.colliderect(box):
        alien.image = 'alien_hurt'
        sounds.eep.play()
    else:
        alien.image = 'alien'
