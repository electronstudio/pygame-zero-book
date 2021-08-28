from mcpi.minecraft import *
from mcpi.block import *

def clear_space(mc, size):
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x-size, pos.y, pos.z-size, pos.x+size, pos.y+size, pos.z+size,
                 AIR)

mc = Minecraft.create()

clear_space(mc, 10)
