# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:23:07 2021

@author: Boksan
"""

broj_ispisa = int(input("Unesite broj ponavljanja: "))

while broj_ispisa <= 0:
    print("Neispravan unos. Unesite ponovo!", end = "\n")
    broj_ispisa = int(input("Unesite broj ponavljanja: "))
    
for i in range(broj_ispisa):
    print("Mi volimo da programiramo!")