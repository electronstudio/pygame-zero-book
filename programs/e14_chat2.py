
from mcpi.minecraft import *

mc = Minecraft.create()

mc.camera.setFixed()

while True:
    events = mc.events.pollChatPosts()


    for event in events:
        print(event)
        command, target = event.message.split()
        #id = mc.getPlayerEntityId(target)
        if command == "build":
            pos = mc.entity.getTilePos(id)
            x = pos.x
            y = pos.y
            z = pos.z
            mc.setBlock(x, y, z, 1)
            mc.postToChat("done building!")
        if command == "follow":
            print("follow")
            id = event.entityId
            mc.camera.setFollow(id)
