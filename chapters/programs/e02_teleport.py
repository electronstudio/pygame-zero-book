from mcpi.minecraft import *

mc = Minecraft.create()

# change these to where you want to go
x = 10
y = 11
z = 12

mc.player.setTilePos(x, y, z)
