# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 22:46:39 2021

@author: Boksan
"""

# napisao sam funkciju koja racuna prosek elemenata na parnim mestima umesto parnih elemenata

def suma_parnih_elemenata(lista:list) -> int:
    suma = 0
    for broj in lista[1::2]:
        suma += broj
    return suma

def prosek(lista:list) -> float:
    return suma_parnih_elemenata(lista)/(len(lista)//2)



lista_brojeva = [12, 44, 91, 66, 1, 123, 52, 214, 410, 6, 22, 100]
print(f"Prosek parnih elemenata liste {lista_brojeva} je {prosek(lista_brojeva)}.")