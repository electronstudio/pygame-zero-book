import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

# CHANGE THESE NUMBERS TO THE CO-ORDS OF YOUR TELEPORTERS

teleporter_x = 742
teleporter_z = 955

destination_x = 735
destination_z = 956

# The main game loop
while True:
    # Short delay to prevent chat filling up too quickly
    time.sleep(0.2)

    # Get player position
    pos = mc.player.getTilePos()
    print(pos)

    # Check whether your player is standing on the teleport
    if pos.x == teleporter_x and pos.z == teleporter_z:
        mc.postToChat("teleport!")
        pos.x = destination_x
        pos.z = destination_z
        mc.player.setTilePos(pos)
