
alien = Actor("alien")
alien.pos = (200, 200)

def draw():
    screen.clear()
    alien.draw()

def update():
    if keyboard.right:
        alien.x = alien.x + 2
    elif keyboard.left:
        alien.x = alien.x - 2

images = ["alien_hurt", "alien"]
image_counter = 0

def animateAlien():
    global image_counter
    alien.image = images[image_counter % len(images)]
    image_counter += 1

clock.schedule_interval(animateAlien, 0.2)
