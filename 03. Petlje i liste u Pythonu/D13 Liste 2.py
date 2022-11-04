# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 23:20:12 2021

@author: Boksan
"""

# a)
lista = list(range(5,30,1))
print(lista[::3])

# b)
pocetak_opsega = int(input("Unesite pocetak opsega: "))
kraj_opsega = int(input("Unesite kraj opsega: "))
while pocetak_opsega < kraj_opsega:
    print("Greska u unosu! Pocetak opsega je manji od kraja opsega.")
    pocetak_opsega = int(input("Unesite pocetak opsega: "))
    kraj_opsega = int(input("Unesite kraj opsega: "))
    
korak = int(input("Unesite korak: "))
while korak < 1:
    print("Korak mora biti 1 ili veci! Unesite ponovo.")
    korak = int(input("Unesite korak: "))

lista2 = list(range(pocetak_opsega, kraj_opsega, -korak))
print(lista2)