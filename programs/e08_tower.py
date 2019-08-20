from mcpi.minecraft import *

mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x + 3
y = pos.y
z = pos.z

for i in range(10):
    mc.setBlock(x, y + i, z, 1)

#TODO
# How high can you make the tower?
# Make the program create 3 towers next to each other

