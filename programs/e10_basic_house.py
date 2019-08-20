from mcpi.minecraft import *
from mcpi.block import *

# This MUST be the name you gave to your clear space program!
from e09_clear_space import *

def make_house(mc, x, y, z, width, height, length):
    mc.setBlocks(x, y, z, x + width, y + height, z + length, STONE)

    # What happens if we make AIR inside the cube?
    mc.setBlocks(x + 1, y + 1, z + 1, x + width - 2, y + height - 2, z + length - 2, AIR)

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

# TODO
# Try bashing a hole in the wall to see what is inside.
# Change the program so it automaticlaly makes a hole for a door.
# Lower the floor in your house.
# Add some furniture, torches, windows.
# Make the windows get bigger if you increase the size of the house
# Try filling a house with LAVA, or WATER, or TNT
# (Becareful with TNT, too much will crash your computer!)