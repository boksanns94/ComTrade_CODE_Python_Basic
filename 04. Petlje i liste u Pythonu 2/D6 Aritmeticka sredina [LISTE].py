# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 22:46:27 2021

@author: Boksan
"""

zbir = 0

uneti_brojevi = [int(input("Unesite broj: "))]

while True:
    if uneti_brojevi[-1] == 0:
        break
    uneti_brojevi.append(int(input("Unesite broj: ")))

if len(uneti_brojevi) == 1:
    print("Nije unet ni jedan broj!")
else:
    for i in range(len(uneti_brojevi)):
        zbir = zbir + uneti_brojevi[i]
    print(f"Aritmeticka sredina unetih brojeva je {zbir/(len(uneti_brojevi)-1):.4f}")