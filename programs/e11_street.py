from mcpi.minecraft import *
from mcpi.block import *

# This MUST be the name you gave to your clear space program!
from clear_space import *
# This MUST be the name you gave to your house program!
from house import *

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
