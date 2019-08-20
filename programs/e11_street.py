from mcpi.minecraft import *
from mcpi.block import *

# This MUST be the name you gave to your clear space program!
from e09_clear_space import *
# This MUST be the name you gave to your house program!
from e10_basic_house import *

mc = Minecraft.create()
pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z

width = 10
height = 5
length = 6

clear_space(mc, 100)

for i in range(1, 100, 20):
    print(x+i, y, z)
    make_house(mc, x+i, y, z, width, height, length)

# TODO
# How many houses are there?  Make the street longer with more houses.
# Make the houses get taller as the street goes on.
# Add some towers to the street.
# Put a loop inside the loop to create multiple streets.
# Copy the make_house function from a friend so you can add a different
#   kind of house to your street.
# Make some roads or fences.
# Make your houses out of TNT.  Use flint tool on them.