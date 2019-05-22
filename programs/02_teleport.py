
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# change these to where you want to go
x = 10
y = 11
z = 12

mc.player.setTilePos(x, y, z)
# TODO
# Find the coordinates of a location in your world, either by pressing F3
# in the game, or running the whereAmI program
# enter them in this program and run it to teleport there
