# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:44:57 2021

@author: Boksan
"""

n = int(input("Unesite n: ")) # unos n
while n <= 0: # provera n
    n = int(input("Pogresan unos! Ponovo: "))

cene_artikala = [] # unos cena artikala
for i in range(n):
    cene_artikala.append(float(input(f"Unesite cenu {i+1}. artikla: "))) # unos cene
    while cene_artikala[-1] <= 0: # provera da li je unos pozitivan
        cene_artikala[-1] = float(input(f"Pogresno. Ponovo {i+1}. artikl: ")) # ispravka

minimalna_cena = cene_artikala[0]
for i in range(1,n):
    if minimalna_cena > cene_artikala[i]:
        minimalna_cena = cene_artikala[i]

print(f"Najjeftiniji artikl kosta {minimalna_cena}.")