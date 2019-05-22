

# The Minecraft API has to be imported before it can be used
import mcpi.minecraft as minecraft

# The time module allows you to insert time delays
import time

# To communicate with a running Minecraft game,
# you need a connection to that game.
mc = minecraft.Minecraft.create()

# A game loop will make sure your game runs forever
while True:
    # delay, to prevent the Minecraft chat filling up too quickly
    time.sleep(1)

    # Ask the Minecraft game for the position of your player
    pos = mc.player.getTilePos()
    print(pos)
    # Display the coordinates of the players position
    mc.postToChat(pos)
