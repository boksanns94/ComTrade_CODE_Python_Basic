# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 22:54:01 2021

@author: Boksan
"""

broj1 = input("Unesite 1. broj: ")
while int(broj1) < 1:
    broj1 = input("Greska. Ponovo: ")
    
broj2 = input("Unesite 2. broj: ")
while int(broj2) < 1:
    broj2 = input("Greska. Ponovo: ")

temp_suma = 0
temp_broj_cifara = 0

for cifra in broj1:
    temp_suma += int(cifra)
    temp_broj_cifara += 1
prosek1 = temp_suma / temp_broj_cifara

for cifra in broj2:
    temp_suma += int(cifra)
    temp_broj_cifara += 1
prosek2 = temp_suma / temp_broj_cifara

if prosek1 > prosek2:
    print(f"Brojevi: {broj1} {broj2}. Prvi broj ima veci prosek cifara -> {prosek1:.2f}.")
elif prosek1 < prosek2:
    print(f"Brojevi: {broj1} {broj2}. Drugi broj ima veci prosek cifara -> {prosek2:.2f}.")
else:
    print(f"Brojevi: {broj1} {broj2}. Brojevi imaju isti prosek cifara -> {prosek1:.2f}.")