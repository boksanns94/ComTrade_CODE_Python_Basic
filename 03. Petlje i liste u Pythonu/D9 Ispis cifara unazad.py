# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:31:04 2021

@author: Boksan
"""

broj = int(input("Unesite broj: "))
if broj < 0:
    temp = -broj
    print("Rezultat: ", end = "")
elif broj == 0:
    print("Rezultat: 0")
else:
    temp = broj
    print("Rezultat: ", end = "")

while temp != 0:
    print(f"{temp%10}", end = " ")
    temp = temp // 10