

import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

# CHANGE THESE NUMBERS TO THE CO-ORDS OF YOUR TELEPORTERS

teleporter_x = 742
teleporter_z = 955

height = 30

while True:
    time.sleep(0.2)

    pos = mc.player.getTilePos()
    print(pos)

    # Check whether your player is standing on the teleport
    if pos.x == teleporter_x and pos.z == teleporter_z:
        mc.postToChat("teleport!")
        pos.y += height  # up in the air!
        pos.x += 1  # move off the teleporter tile
        mc.player.setTilePos(pos)
