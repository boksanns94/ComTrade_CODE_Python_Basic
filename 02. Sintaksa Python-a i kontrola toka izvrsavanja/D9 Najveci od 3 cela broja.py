# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 16:34:20 2021

@author: Boksan
"""

broj1 = int(input("Unesite prvi broj: "))
broj2 = int(input("Unesite drugi broj: "))
broj3 = int(input("Unesite treci broj: "))

if broj1 >= broj2 and broj1 >= broj3:
    print(f"Broj 1: {broj1}, je najveci.")
elif broj2 >= broj3:
    print(f"Broj 2: {broj2}, je najveci.")
else:
    print(f"Broj 3: {broj3}, je najveci.")
