# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 18:27:07 2021

@author: Boksan
"""

broj = int(input("Unesite pozitivan ceo broj: "))

while broj <= 0:
    print("Greska pri unosu! Unesite ponovo.")
    broj = int(input("Unesite pozitivan ceo broj: "))

if broj == 1:
    print("Delioc broja 1 je: 1.")
elif broj < 3:
    print(f"Delioci broja {broj} su: 1, {broj}.")
else:
    print(f"Delioci broja {broj} su: 1, ", end = "")
    for delioc in range(4, broj):
        if broj % delioc == 0:
            print(f"{delioc}, ", end = "")
print(f"{broj}.")