# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:21:08 2020

@author: user
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z-1,38)
time.sleep(0.2)