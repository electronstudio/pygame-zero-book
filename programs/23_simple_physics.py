WIDTH = 500
HEIGHT = 500

ball = Rect((200, 400), (20, 20))
vx = 1
vy = 1

def draw():
    screen.clear()
    screen.draw.filled_rect(ball, "red")

def update():
    global vx, vy
    ball.x += vx
    ball.y += vy
    if ball.right > WIDTH or ball.left < 0:
        vx = -vx
    if ball.bottom > HEIGHT or ball.top < 0:
        vy = -vy
