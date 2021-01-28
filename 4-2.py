from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()
import random

x,y,z = cherinehsu.player.getTilePos()

for i in range(450):
    r = random.randrange(1,7)
    if r == 1:
        cherinehsu.setBlocks(x,y,z,x,y,z+4,57)
        z = z+4
    if r == 2:
        cherinehsu.setBlocks(x,y,z,x,y,z-4,29)
        z = z-4
    if r == 3:
        cherinehsu.setBlocks(x,y,z,x+4,y,z,41)
        x = x+4
    if r == 4:
        cherinehsu.setBlocks(x,y,z,x-4,y,z,88)
        x = x-4
    if r == 5:
        cherinehsu.setBlocks(x,y,z,x,y+4,z,46)
        y = y+4    
    if r == 6:
        cherinehsu.setBlocks(x,y,z,x,y-4,z,35)
        y = y-4