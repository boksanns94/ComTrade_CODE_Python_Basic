# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:51:24 2021

@author: Boksan
"""

broj_transakcija = int(input("Unesite broj transakcija: "))

if broj_transakcija == 0:
    print("Nema evidentiranih transakcija!")
    exit()
else:
    while broj_transakcija < 0:
        print("Neispravan unos! Unesite ponovo.")
        broj_transakcija = int(input("Unesite broj transakcija: "))

    prihod = 0
    rashod = 0
    for i in range(broj_transakcija):
        temp = int(input(f"Unesite {i+1}. transakciju: "))
        if temp > 0:
            prihod = prihod + temp
        else:
            rashod = rashod - temp

    print()
    print(f"Prihod firme je bio {prihod} dinara.")
    print(f"Rashod firme je bio {-rashod} dinara.")
    if prihod - rashod >= 0:
        print(f"Zarada firme je bila {prihod-rashod} dinara.")
    else:
        print(f"Gubitak firme je bio {prihod-rashod} dinara.")