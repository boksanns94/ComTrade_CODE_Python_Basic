# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:20:03 2021

@author: Boksan
"""

# korisnik unos n, napraviti date sablone

n = int(input("Unesite n: "))
while n < 3: # vrednosti 2 i manje ne mogu da iscrtaju krst
    n = int(input("Greska. Ponovo: "))

if n % 2 == 0:
    for i in range(n):
        if i == n//2 or i == n//2-1: # dva srednja reda
            print(n*"*") # popunimo red zvezdicama
        else: # svi ostali redovi
            print(f"{'**':^{n}}") # stampam 2 zvezdice i centriram u n polja
else:
    for i in range(n):
        if i == n//2: # srednji red
            print(n*"*") # popunimo red zvezdicama
        else: # svi ostali redovi
            print(f"{'*':^{n}}") # stampam 1 zvezdicu, centriranu u n polja