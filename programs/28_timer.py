# Pygame can tell us how much time has passed since the last frame
# in a parameter to our update function. We use this to keep a timer.

timer = 0

def update(dt):
    global timer
    timer += dt


def draw():
    screen.clear()
    screen.draw.text(f"Time passed: {timer}", (0, 0))
    if timer > 5:
        screen.draw.textbox("Time's up!", Rect(50, 50, 200, 200))

# TODO
# Make the timer count down, not up.
# Add a timer to one of your other games.
# Add a timer to program 21 that deletes one of the aliens when the timer runs out
#   then starts the timer again.
