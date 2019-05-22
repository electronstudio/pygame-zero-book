

import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

# CHANGE THESE NUMBERS TO THE CO-ORDS OF YOUR TELEPORTERS

teleporter_x = 742
teleporter_z = 955

height = 20

while True:
    time.sleep(0.2)

    pos = mc.player.getTilePos()

    if pos.x == teleporter_x and pos.z == teleporter_z:
        mc.postToChat("teleport!")
        pos.x += 1  # move off the teleporter tile
        for i in range(0,height):
            pos.y += 1  # move up a bit
            time.sleep(0.05)
            mc.player.setTilePos(pos)

# TODO
# change the height of the jump
# move the player in X and Z directions as well
# during the jump
