# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:43:16 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

mc.setBlocks(x+100,y-1,z+100,x-100,y-1,z-100,46)