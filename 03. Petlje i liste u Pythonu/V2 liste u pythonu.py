# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 19:30:34 2021

@author: Boksan
"""

#liste se deklarisu uglastim zagradama
voce = ["narandza", "jabuka", "malina", "dunja", "kajsija", "tresnja", "breskva"]
print(voce)
print(voce[0]) #istampace "narandza"

broj_elemenata_liste = len(voce)
print(broj_elemenata_liste)

#poslednji element liste
print("Poslednji element liste: ", voce[broj_elemenata_liste-1])
print("Poslednji element liste: ", voce[-1])

#slajsovanje listi
print(voce[1:4:2]) #ispisace od 1 do 3 sa korakom 2
print(voce[-1:1:-1]) #ispisace od 5 do 1 sa korakom 1, ali unazad
print(voce[2:4]) #korak se podrazumeva da je 1
print(voce[:3]) #prvi argument se smatra pocetkom liste ako se izostavi
print(voce[:4:1])
print(voce[3:]) #drugi argument se smatra krajem liste ako se izostavi
print(voce[3::1])
print(voce[::]) #ispisuje celu listu
print(voce[::-1]) #ispisuje celu listu unazad
print(voce[:2:-1]) #ako pocetak nije naveden, a korak je negativan, podrazumeva se
                    # da je pocetak ustvari kraj liste

#provera palindroma
palindrom = "anavolimilovana"
if palindrom == palindrom[::-1]:
    print("Jeste palindrom.")
else:
    print("Nije palindrom.")

#prvi nacin prolaska kroz listu
#prolazak kroz listu preko pozicija
duzina = len(voce)
for i in range(duzina):
    print(voce[i], end = " ")

print()
#drugi nacin prolaska kroz listu
#prolazak kroz listu preko privremene promenljive u for-u
for vocka in voce:
    print(vocka, end = " ")