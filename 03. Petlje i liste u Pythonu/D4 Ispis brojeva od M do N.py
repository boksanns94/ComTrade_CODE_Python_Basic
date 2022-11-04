# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:45:56 2021

@author: Boksan
"""

pocetak_opsega = int(input("Unesite pocetak opsega: "))
kraj_opsega = int(input("Unesite kraj opsega: "))

while pocetak_opsega > kraj_opsega:
    print("Pogresan unos granica! Unesite ponovo.", end = "\n")
    pocetak_opsega = int(input("Unesite pocetak opsega: "))
    kraj_opsega = int(input("Unesite kraj opsega: "))

print("\nStampa preko FOR petlje:")
for i in range(pocetak_opsega, kraj_opsega+1):
    print(i)

print("\nStampa preko WHILE petlje:")
i = pocetak_opsega
while i <= kraj_opsega:
    print(i)
    i = i+1