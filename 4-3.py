from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()
from random import randrange

for i in range(10):
    x,y,z = cherinehsu.player.getTilePos()
    z = z+i
    for j in range(10):
        color = randrange(0,16)
        x = x+1
        cherinehsu.setBlock(x,y,z,35,color)

ans = randrange(0,16)
while True:
    hits = cherinehsu.events.pollBlockHits()
    if len(hits)>0:
        h = hits[0]
        block = cherinehsu.getBlockWithData(h.pos)
        data = block.data
        
        if data == ans :
            cherinehsu.postToChat("恭喜你找到啦!")
            cherinehsu.setBlock(h.pos,57) 
            break
        
        elif data < ans:
           cherinehsu.postToChat("找錯囉~找大一點的吧!") 
        elif data > ans:
           cherinehsu.postToChat("找錯囉~找小一點的吧!")