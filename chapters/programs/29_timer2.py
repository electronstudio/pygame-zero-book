
import random

aliens = []

def add_alien():
    aliens.append(
        Actor("alien", (random.randint(0,500), random.randint(0,500)))
    )

# call add_alien once, 0.5 seconds from now
clock.schedule(add_alien, 0.5)

# call add_alien over and over again, ever 2 seconds
clock.schedule_interval(add_alien, 2.0)

def draw():
    screen.clear()
    for alien in aliens:
        alien.draw()
