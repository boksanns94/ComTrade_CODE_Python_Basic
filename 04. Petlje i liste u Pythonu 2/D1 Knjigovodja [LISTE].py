# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:45:56 2021

@author: Boksan
"""

broj_transakcija = int(input("Unesite broj transakcija: "))

if broj_transakcija == 0:
    print("Nema evidentiranih transakcija!")
    exit()
else:
    transakcije = []
    while broj_transakcija < 0:        
        print("Neispravan unos! Unesite ponovo.")
        broj_transakcija = int(input("Unesite broj transakcija: "))

    prihod = 0
    rashod = 0
    
    for i in range(broj_transakcija):
        transakcije.append(int(input(f"Unesite {i+1}. transakciju: ")))
        
    for i in range(broj_transakcija):
        if transakcije[i] > 0:
            prihod = prihod + transakcije[i]
        else:
            rashod = rashod - transakcije[i]
    
    print()
    print(f"Prihod firme je bio {prihod} dinara.")
    print(f"Rashod firme je bio {-rashod} dinara.")
    if prihod - rashod >= 0:
        print(f"Zarada firme je bila {prihod-rashod} dinara.")
    else:
        print(f"Gubitak firme je bio {prihod-rashod} dinara.")