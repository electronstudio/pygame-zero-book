import pygame

WIDTH = 500
HEIGHT = 500

alien = Actor("alien")

fs = False

def draw():
    screen.clear()
    alien.draw()

def update():
    global fs
    if not fs:
        pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        fs = True
    if keyboard.escape:
        exit()
