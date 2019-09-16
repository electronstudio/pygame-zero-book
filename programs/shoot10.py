import random

WIDTH = 600
HEIGHT = 800
MAX_BULLETS = 3

level = 0
lives = 3
score = 0
time = 20

background = Actor("background")
player = Actor("player", (200,780))

enemies = []
bullets = []
bombs = []

def draw():
    screen.clear()
    background.draw()
    player.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    for bomb in bombs:
        bomb.draw()
    draw_text()

def update(delta):
    if len(enemies)==0:
        create_enemies()
    move_player()
    move_bullets()
    move_enemies()
    create_bombs()
    move_bombs()


def create_enemies():
    global level
    level = level + 1
    for x in range(0,600, 60):
        for y in range(0,200, 60):
            enemy = Actor("alien", (x, y))
            enemy.vx = level * 2
            enemies.append(enemy)


def on_key_down(key):
    if(key==keys.SPACE and len(bullets) < MAX_BULLETS):
        bullet = Actor("alien", pos=(player.x, player.y))
        bullets.append(bullet)



def move_player():
    if keyboard.right:
        player.x = player.x + 5
    if keyboard.left:
        player.x = player.x - 5

    if player.x > WIDTH:
        player.x = WIDTH
    if player.x < 0:
        player.x = 0

def move_bullets():
    pass

def create_bombs():
    pass
def move_bombs():
    pass

def move_enemies():
    global score
    for enemy in enemies:
        enemy.x = enemy.x + enemy.vx
        if enemy.x > WIDTH or enemy.x < 0:
            enemy.vx = -enemy.vx
            animate(enemy, duration=0.1, y=enemy.y+60)
        for bullet in bullets:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score = score + 1
        if enemy.colliderect(player):
            exit()



def draw_text():
    pass


