# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 20:44:43 2021

@author: Boksan
"""

n = int(input("Unesite broj n: "))
while n <= 0:
    print("Neispravan unos! Unesite ponovo.")
    n = int(input("Unesite broj n: "))

zbir = 0
for i in range(n):
    broj = int(input(f"Unesite {i+1}. broj: "))
    if broj < 0 and broj % 2 != 0:
        zbir = zbir + broj

print(f"Zbir brojeva koji su i neparni i negativni je: {zbir}.")