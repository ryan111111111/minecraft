# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:50:33 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,0,"我愛","minecraft","也愛","python")