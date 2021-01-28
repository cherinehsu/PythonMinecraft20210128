from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()
import random

x,y,z = cherinehsu.player.getTilePos()

for i in range(20):
    r = random.randrange(1,5)
    if r == 1:
        cherinehsu.setBlocks(x,y,z,x,y,z+4,41)
        z = z+4
    if r == 2:
        cherinehsu.setBlocks(x,y,z,x,y,z-4,41)
        z = z-4
    if r == 3:
        cherinehsu.setBlocks(x,y,z,x+4,y,z,41)
        x = x+4
    if r == 4:
        cherinehsu.setBlocks(x,y,z,x-4,y,z,41)
        x = x-4