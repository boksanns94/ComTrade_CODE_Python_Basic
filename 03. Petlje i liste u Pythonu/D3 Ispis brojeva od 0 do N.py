# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:26:45 2021

@author: Boksan
"""

broj = int(input("Unesite broj: "))

while broj <= 0:
    print("Pogresan unos! Unesite ponovo.", end = "\n")
    broj = int(input("Unesite broj: "))

for i in range(broj+1):
    print(i)