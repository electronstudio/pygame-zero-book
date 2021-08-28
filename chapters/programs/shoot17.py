WIDTH = 600
HEIGHT = 800

background = Actor("background")
player = Actor("player", (300,780))
enemies = []
bullets = []
bombs = []
explosions = []

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
    for explosion in explosions:
        explosion.draw()
    draw_text()

def update():
    move_player()
    move_bullets()
    move_enemies()
    create_bombs()
    move_bombs()
    animate_explosions()
    check_for_end_of_level()

def check_for_end_of_level():
    pass

def move_player():
    pass

def move_bullets():
    pass

def create_bombs():
    pass

def move_bombs():
    pass

def move_enemies():
    pass

def draw_text():
    pass

def animate_explosions():
    pass


