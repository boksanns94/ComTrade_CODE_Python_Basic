# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 23:06:10 2021

@author: Boksan
"""

broj = int(input("Unesite ceo broj: "))
while broj < 1:
    broj = int(input("Greska. Ponovo: "))

for i in range(broj):
    trenutni_kvadrat = (i+2)**2 # u prvom krugu nema smisla kretati ni od 0, ni od 1
    if trenutni_kvadrat > broj//2:              # ako je kvadrat koji trenutno ispitujemo veci od polovine
        print(f"Broj {broj} je bezkvadratan.")  # broja, taj kvadrat ne moze biti delioc tog broja
        break                                   # i u tom momentu mozemo prekinuti pretragu
    else:
        if broj % trenutni_kvadrat == 0:
            print(f"Broj {broj} nije bezkvadratan. Deljiv je sa {trenutni_kvadrat} ({i+2}*{i+2})")
            break # cim naidjemo na jedno resenje odma zavrsavamo petlju