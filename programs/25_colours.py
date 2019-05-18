# my_colour = (0,0,0) # makes black
# my_colour = (255,255,255) # makes white

red_amount = 0
green_amount = 0
blue_amount = 0

def draw():
    my_colour = (red_amount, green_amount, blue_amount)
    screen.fill(my_colour)

# This function makes the colour change every frame
# Remove it if you just want to see a static colour.
def update():
    global red_amount
    red_amount += 1
    red_amount = red_amount % 255

