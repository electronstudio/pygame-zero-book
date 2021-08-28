from mcpi.minecraft import *

mc = Minecraft.create()

while True:
    events = mc.events.pollChatPosts()
    for event in events:
        print(event)
        if event.message == "build":
            id = event.entityId
            pos = mc.entity.getTilePos(id)
            x = pos.x
            y = pos.y
            z = pos.z
            mc.setBlock(x, y, z, 1)
            mc.postToChat("done building!")
