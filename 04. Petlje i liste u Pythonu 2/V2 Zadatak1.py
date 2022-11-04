# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 20:35:23 2021

@author: Boksan
"""

# Korisnik unos n a zatim n celih brojeva u listu
# 1 izracunati prosek elemenata koji su veci od razlike 1 i poslednjeg
# 2 izracunati proizvod elemenata koji su manji od proseka iz tacke 1

n = int(input("Unesite n: "))
while n <= 0:
    n = int(input("Unesite pozitivan n: "))
brojevi = []

# pravimo listu
for i in range(n):
    brojevi.append(int(input(f"Unesite {i+1}. element: ")))

# inicijalizujemo elemente za trazenje proseka
granica_proseka = brojevi[-1] - brojevi[0]
zbir_vecih_od_razlike = 0
broj_elemenata_zbira = 0

# trazimo prosek
for broj in brojevi:
    if broj > granica_proseka:
        zbir_vecih_od_razlike = zbir_vecih_od_razlike + broj
        broj_elemenata_zbira = broj_elemenata_zbira + 1
if broj_elemenata_zbira > 0:
    prosek = zbir_vecih_od_razlike/broj_elemenata_zbira
    print(f"Zbir: {zbir_vecih_od_razlike}, Broj: {broj_elemenata_zbira}")
    print(f"Prosek je: {prosek}")
else:
    print("Ni jedan element nije veci od razlike poslednjeg i prvog.")

print()

# racunanje proizvoda elemenata manjih od proseka
proizvod_manjih_od_proseka = 1
broj_elemenata_proizvoda = 0
for broj in brojevi:
    if broj < prosek:
        proizvod_manjih_od_proseka = proizvod_manjih_od_proseka * broj
        broj_elemenata_proizvoda = broj_elemenata_proizvoda + 1
if broj_elemenata_proizvoda > 0:
    print(f"Proizvod elemenata manjih od proseka je: {proizvod_manjih_od_proseka}.")
else:
    print("Ni jedan element nije manji od proseka.")