# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 18:39:10 2021

@author: Boksan
"""

# data je lista brojeva. korisnik unosi broj.
# ispitati da li je broj u listi bez koriscenja operatora in

brojevi = [1,5,11,2,33,26,83,44,23,893,7,123,111,234,55]

trazeni_broj = int(input("Unesite trazeni broj: "))
broj_jeste_u_listi = False

for i in range(len(brojevi)):
    if trazeni_broj == brojevi[i]:
        broj_jeste_u_listi = True
        break

if broj_jeste_u_listi:
    print(f"Broj {trazeni_broj} jeste u listi {brojevi}.")
else:
    print(f"Broj {trazeni_broj} nije u listi {brojevi}.")