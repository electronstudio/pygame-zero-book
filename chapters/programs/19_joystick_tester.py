import pygame

def update():
    screen.clear()
    joystick_count = pygame.joystick.get_count()
    y = 0
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        name = joystick.get_name()
        axes = joystick.get_numaxes()
        buttons = joystick.get_numbuttons()
        hats = joystick.get_numhats()
        screen.draw.text(
            "Joystick {} name: {} axes:{} buttons:{} hats:{}".format(
                i, name, axes, buttons, hats), (0, y))
        y += 14
        for i in range(axes):
            axis = joystick.get_axis(i)
            screen.draw.text("Axis {} value: {:>6.3f}".format(i, axis),
                             (20, y))
            y += 14
        for i in range(buttons):
            button = joystick.get_button(i)
            screen.draw.text("Button {:>2} value: {}".format(i, button),
                             (20, y))
            y += 14
        for i in range(hats):
            hat = joystick.get_hat(i)
            screen.draw.text("Hat {} value: {}".format(i, str(hat)),
                             (20, y))
            y += 14
