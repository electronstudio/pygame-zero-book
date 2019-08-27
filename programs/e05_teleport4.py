
from mcpi.minecraft import *
import time

mc = Minecraft.create()

# CHANGE THESE NUMBERS TO THE CO-ORDS OF YOUR TELEPORTERS

teleporter_x = 9
teleporter_z = 12

height = 20

while True:
    pos = mc.player.getTilePos()

    if pos.x == teleporter_x and pos.z == teleporter_z:
        mc.postToChat("teleport!")
        # move off the teleporter tile so we dont land on it again
        pos.x += 1
        for i in range(0, height):
            pos.y += 1  # move up a bit
            time.sleep(0.1) # short delay of 0.2 seconds
            mc.player.setTilePos(pos)
