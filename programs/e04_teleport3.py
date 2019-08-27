
from mcpi.minecraft import *

mc = Minecraft.create()

# CHANGE THESE NUMBERS TO THE CO-ORDS OF YOUR TELEPORTERS

teleporter_x = 9
teleporter_z = 12

height = 30

while True:
    pos = mc.player.getTilePos()

    # Check whether your player is standing on the teleport
    if pos.x == teleporter_x and pos.z == teleporter_z:
        mc.postToChat("teleport!")
        pos.y += height  # up in the air!
        pos.x += 1  # move off the teleporter tile
        mc.player.setTilePos(pos)
