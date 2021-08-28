import pygame

WIDTH = 500
HEIGHT = 500

alien = Actor("alien")

def draw():
    screen.clear()
    alien.draw()

def update():
    if keyboard.f:
        pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    if keyboard.escape:
        exit()
