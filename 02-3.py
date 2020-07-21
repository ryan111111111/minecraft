# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:43:43 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
height=10
widht=10
lenght=10
mc.setBlocks(x,y,z,x+widht,y+height,z+lenght,35)
mc.setBlocks(x+1,y+1,z+1,x-widht,y-height,z-lenght,35)