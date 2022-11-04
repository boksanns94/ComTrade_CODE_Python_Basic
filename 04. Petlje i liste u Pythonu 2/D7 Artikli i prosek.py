# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:04:06 2021

@author: Boksan
"""

cene_artikala = [float(input("Unesite cenu artikla: "))]

#unos cena artikala
while True:
    while cene_artikala[-1] < 0: # ako je cena poslednjeg negativna, ponavljamo unos
        cene_artikala[-1] = float(input("Pogresan unos. Ponovo: "))
    if cene_artikala[-1] == 0: # ako se unese nula, prekida se unos
        break
    cene_artikala.append(float(input("Unesite cenu artikla: "))) # unos normalne cene

suma = 0
for i in range(len(cene_artikala)-1):   # racunanje zbira svih elemenata osim poslednjeg
    suma = suma + cene_artikala[i]      # jer je poslednji 0

print(f"Prosecna cena: {suma/(len(cene_artikala)-1)}.") # prosek u f stringu