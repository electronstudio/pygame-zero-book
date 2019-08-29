
from mcpi.minecraft import *
from mcpi.block import *

mc = Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    blocktype = WOOL
    mc.setBlock(x, y, z, blocktype)
