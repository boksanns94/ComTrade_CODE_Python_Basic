# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:38:13 2021

@author: Boksan
"""

broj = int(input("Unesite broj: "))

while broj <= 0:
    print("Pogresan unos! Unesite ponovo.")
    broj = int(input("Unesite broj: "))
    
temp = broj

zbir_cifara = 0
while temp != 0:
    zbir_cifara = zbir_cifara + temp % 10
    temp = temp // 10
    
if broj % zbir_cifara == 0:
    print(f"Broj {broj} je deljiv sa zbirom njegovih cifara, {zbir_cifara}.")
else:
    print(f"Broj {broj} nije deljiv sa zbirom njegovih cifara, {zbir_cifara}.")