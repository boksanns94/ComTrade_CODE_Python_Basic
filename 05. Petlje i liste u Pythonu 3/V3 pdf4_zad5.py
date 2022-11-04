# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:10:17 2021

@author: Boksan
"""

# napisati program koji ucitava br n, a zatim listu od n znakova
# nakon toga se unosi rec, proveriti da li se rec moze napisati
# od znakova iz liste

n = int(input("Unesite n: "))
while n <= 0:
    n = int(input("Greska unosa n. Ponovo: "))

lista_znakova = []
for i in range(n):
    lista_znakova.append(input(f"Unesite {i+1}. znak: "))

trazena_rec = input("Unesite trazenu rec: ")
moze_da_se_napise_rec = True
for slovo in trazena_rec:
    if slovo not in lista_znakova:
        moze_da_se_napise_rec = False
        break

if moze_da_se_napise_rec:
    print(f"Rec {trazena_rec} moze da se napise od znakova iz liste {lista_znakova}.")
else:
    print(f"Rec {trazena_rec} ne moze da se napise od znakova iz liste {lista_znakova}.")