from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()

list2 = [[22,41,133],[35,57,42]]

myID = cherinehsu.getPlayerEntityId("cherinehsu")
x,y,z = cherinehsu.entity.getTilePos(myID)


startX = x
for i in list2:
    for j in i:
        
        cherinehsu.setBlock(x,y,z,j)
        x = x+1
    x = startX
    z = z-1