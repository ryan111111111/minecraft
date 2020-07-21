# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:59:33 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while true:
    x,y,z=mc.player.getTilePos()
    a=mc.getBlock(x+1,y-1,z)
    b=mc.getBlock(x-1,y-1,z)
    c=mc.getBlock(x,y-1,z+1)
    d=mc.getBlock(x,y-1,z-1)
    if a==9 or b==9 or c==9 or d==9:
        mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,79)
    
    
    
    