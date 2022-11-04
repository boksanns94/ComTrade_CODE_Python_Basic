# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 22:40:22 2021

@author: Boksan
"""

#sumu svih parnih
#proizvod svih neparnih

broj = input("Unesite broj: ")
while broj < 1:
    broj = input("Greska. Ponovo: ")

neparna_pozicija = True
proizvod_neparnih = 1
zbir_parnih = 0

for cifra in broj: # vadim jednu po jednu cifru
    if neparna_pozicija: # ako je na neparnoj poziciji
        proizvod_neparnih *= int(cifra) # mnozim cifru
        neparna_pozicija = not neparna_pozicija # sledeca pozicija je parna
    else: # ako je na parnoj poziciji
        zbir_parnih += int(cifra) # sabiram cifru
        neparna_pozicija = not neparna_pozicija # sledeca pozicija je neparna

print(f"Zbir svih cifara na parnim pozicijama broja {broj} je {zbir_parnih}.")
print(f"Proizvod svih cifara na neparnim pozicijama broja {broj} je {proizvod_neparnih}.")