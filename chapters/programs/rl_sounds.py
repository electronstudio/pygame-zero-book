from richlib import *
sound = Sound('eep')
sound.volume = 0.7
sound.pitch = 0.5

def draw():
    clear()

def update():
    if mouse.clicked:
        sound.play()
run()