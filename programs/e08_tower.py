from mcpi.minecraft import *

mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x + 3
y = pos.y
z = pos.z

for i in range(10):
    mc.setBlock(x, y + i, z, 1)
