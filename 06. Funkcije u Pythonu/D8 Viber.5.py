# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 23:11:16 2021

@author: Boksan
"""

# napisati program koji racuna prosek parnih elemenata liste

def suma_parnih_elemenata(lista:list) -> None:
    global suma             # znam da ne moram da pravim globalne promenljive
    global broj_elemenata   # zeleo sam prosto malo da ih probam kako rade
    for broj in lista:
        if broj % 2 == 0:
            suma += broj
            broj_elemenata += 1

def prosek_parnih_elemenata(lista:list) -> None:
    global prosek
    global suma
    global broj_elemenata
    suma_parnih_elemenata(lista)
    prosek = suma / broj_elemenata



lista_brojeva = [12, 44, 91, -66, -1, 123, 52, -214, 411, 55, 6, 22, 100, -27]
suma = 0
broj_elemenata = 0
prosek = 0
prosek_parnih_elemenata(lista_brojeva)
print(f"Suma parnih elemenata: {suma}")
print(f"Broj parnih elemenata: {broj_elemenata}.")
print(f"Prosek parnih elemenata liste {lista_brojeva} je {prosek}.")