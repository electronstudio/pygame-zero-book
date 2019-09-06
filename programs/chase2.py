WIDTH = 600
HEIGHT = 600

background = Actor("background")
player = Actor("player")
player.x = 200
player.y = 200


def draw():
    screen.clear()
    background.draw()
    player.draw()



def update():
    global score
    if keyboard.right:
        player.x = player.x + 4
    if keyboard.left:
        player.x = player.x - 4
    if keyboard.down:
        player.y = player.y + 4
    if keyboard.up:
        player.y = player.y - 4

    if player.x > WIDTH:
        player.x = 0
    if player.x < 0:
        player.x = WIDTH
    if player.y < 0:
        player.y = HEIGHT
    if player.y > HEIGHT:
        player.y = 0


