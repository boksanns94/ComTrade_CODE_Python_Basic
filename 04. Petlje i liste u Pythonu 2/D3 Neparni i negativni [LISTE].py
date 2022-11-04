# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:56:30 2021

@author: Boksan
"""

n = int(input("Unesite broj n: "))
while n <= 0:
    print("Neispravan unos! Unesite ponovo.")
    n = int(input("Unesite broj n: "))

spisak_brojeva = []
for i in range(n):
    spisak_brojeva.append(int(input(f"Unesite {i+1}. broj: ")))

zbir = 0
for i in range(n):
    if spisak_brojeva[i] < 0 and spisak_brojeva[i] % 2 != 0:
        zbir = zbir + spisak_brojeva[i]

print(f"Zbir brojeva koji su i neparni i negativni je: {zbir}.")