# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 18:47:16 2021

@author: Boksan
"""

def min(x,y,z):
    trenutni_minimum = x
    if trenutni_minimum > y:
        trenutni_minimum = y
    if trenutni_minimum > z:
        trenutni_minimum = z
    return trenutni_minimum

najmanji = min(10,3,-4)
print(najmanji)

broj1 = int(input("Prvi broj: "))
broj2 = int(input("Drugi broj: "))
broj3 = int(input("Trecu broj: "))
najmanji = min(broj1, broj2, broj3)
print(najmanji)