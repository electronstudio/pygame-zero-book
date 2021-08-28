import pygame
WIDTH = 500
HEIGHT = 500

joystick = pygame.joystick.Joystick(0)
joystick.init()

alien = Actor("alien")
alien.pos = (0, 50)

def draw():
    screen.clear()
    alien.draw()

def update():
    if keyboard.right or joystick.get_axis(0) > 0.1:
        alien.x = alien.x + 2
    elif keyboard.left or joystick.get_axis(0) < -0.1:
        alien.x = alien.x - 2

