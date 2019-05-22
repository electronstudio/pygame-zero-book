
from mcpi.minecraft import Minecraft
import time
import mcpi.block as block

mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

while True:
    time.sleep(0.2)
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    blockType = 10
    mc.setBlock(x, y, z, block.LAVA)

# TODO
# Make the block appear one unit BELOW the player's position
# Change the block to something else.  Ice?
