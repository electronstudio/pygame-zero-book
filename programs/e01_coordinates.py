# Get the player's co-ordinates
# Print them to the chat

from mcpi.minecraft import *
import time

mc = Minecraft.create()

while True:     # loop will make sure your game runs forever
    time.sleep(1)
    pos = mc.player.getTilePos()
    print(pos)
    mc.postToChat(pos)
