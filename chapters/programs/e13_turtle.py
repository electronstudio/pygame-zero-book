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
