# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 18:25:11 2021

@author: Boksan
"""

# korisnik unosi n, a zatim i n celih brojeva
# ipsitati da li je lista rastuca

n = int(input("Unesite n: "))
while n <= 0:
    n = int(input("Pogresan unos. Ponovo: "))

brojevi = []
for i in range(n):
    brojevi.append(int(input(f"Unesite {i+1}. element: ")))

lista_opadajuca = False
for i in range(n-1):
    if brojevi[i] > brojevi[i+1]:
        lista_opadajuca = True
        break

if lista_opadajuca:
    print("Lista nije neopadajuca.")
else:
    print("Lista jeste neopadajuca.")