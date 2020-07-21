# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:10:41 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random

while True:
    x,y,z=mc.player.getTilePos()
    color=random.randrange(1,15)
    mc.setBlocks(x+10,y-1,z+10,x-10,y-1,z-10,46,color)