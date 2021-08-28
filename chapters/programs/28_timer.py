
timer = 0

def update(dt):
    global timer
    timer += dt


def draw():
    screen.clear()
    screen.draw.text(f"Time passed: {timer}", (0, 0))
    if timer > 5:
        screen.draw.textbox("Time's up!", Rect(50, 50, 200, 200))
