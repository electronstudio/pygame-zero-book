from mcpi.minecraft import *
from mcpi.block import *

# This MUST be the name you gave to your clear space program!
from clear_space import *

def make_house(mc, x, y, z, width, height, length):
    mc.setBlocks(x, y, z, x + width, y + height, z + length, STONE)

    # What happens if we make AIR inside the cube?
    mc.setBlocks(x + 1, y + 1, z + 1,
                 x + width - 2, y + height - 2, z + length - 2, AIR)

mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

width = 10
height = 50
length = 60

# Use the function from the other program
clear_space(mc, 10)
make_house(mc, x, y, z, width, height, length)
