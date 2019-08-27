
from mcpi.minecraft import *
from mcpi.block import *

mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
blocktype = 1
mc.setBlock(x, y, z, blocktype)
