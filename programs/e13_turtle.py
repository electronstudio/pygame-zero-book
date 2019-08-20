# THIS REQUIRES THE MINCRAFTSTUFF PACKAGE TO WORK
# You can install it in Mu by clicking in the bottom right gadget
#   and adding mincraftstuff to list of third party packages

# You may have used a turtle for drawing at school.
# This is the same but in MInecraft.

from mcpi.minecraft import *
from mcpi.block import *

from minecraftstuff import MinecraftTurtle

mc = Minecraft.create()
pos = mc.player.getTilePos()
pos.y += 1

turtle = MinecraftTurtle(mc, pos)

turtle.forward(5)
turtle.right(90)
turtle.forward(5)
turtle.right(90)
turtle.forward(5)
turtle.right(90)
turtle.forward(5)

# TODO
# Draw a triangle, hexagon, etc.
# What do turtle.up(90) and turtle.down(90) do?