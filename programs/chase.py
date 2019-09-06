WIDTH = 600
HEIGHT = 600

background = Actor("background")
player = Actor("player")
player.x = 200
player.y = 200
score = 0

badguy = Actor("badguy")

def draw():
    screen.clear()
    background.draw()
    player.draw()
    badguy.draw()
    screen.draw.text(f"score: {score}", (0,0), color='red')

def update():
    global score
    if keyboard.right:
        player.x = player.x + 6
    if keyboard.left:
        player.x = player.x - 6
    if keyboard.down:
        player.y = player.y + 6
    if keyboard.up:
        player.y = player.y - 6

    if keyboard.d:
        badguy.x = badguy.x + 5
    if keyboard.a:
        badguy.x = badguy.x - 5
    if keyboard.s:
        badguy.y = badguy.y + 5
    if keyboard.w:
        badguy.y = badguy.y - 5

    if player.x > 600:
        player.x = 0
    if player.x < -36:
        player.x = 600
    if player.y < -36:
        player.y = 600
    if player.y > 636:
        player.y = 0

    print(player.x, player.y)

    if badguy.x > 600:
        badguy.x = 0
    if badguy.x < -36:
        badguy.x = 600
    if badguy.y < -36:
        badguy.y = 600
    if badguy.y > 636:
        badguy.y = 0

    if badguy.colliderect(player):
        sounds.eep.play()


