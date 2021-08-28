WIDTH = 500
HEIGHT = 500

class Sprite(Actor):
    vx = 1
    vy = 1

    def update(self):
        self.x += self.vx
        self.y += self.vy
        if self.right > WIDTH or self.left < 0:
            self.vx = -self.vx
        if self.bottom > HEIGHT or self.top < 0:
            self.vy = -self.vy

ball = Sprite("alien")

def draw():
    screen.clear()
    ball.draw()

def update():
    ball.update()
