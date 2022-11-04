# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 22:22:30 2021

@author: Boksan
"""

def broj_cifara(broj:int) -> int:
    if broj < 0:            # ako korisnik unese negativan broj
        broj *= -1
    return len(str(broj))

def armstrongova_suma(broj:int) -> int:
    armstrongova_suma = 0
    for cifra in str(broj):
        if cifra == "-":    # ako korisnik unese negativan broj
            continue
        armstrongova_suma += int(cifra)**broj_cifara(broj)
    return armstrongova_suma

def najveca_armstrongova_suma(lista_brojeva:list) -> int:
    najveci_broj = lista_brojeva[0]
    for broj in lista_brojeva:
        if armstrongova_suma(broj) > armstrongova_suma(najveci_broj):
            najveci_broj = broj
    return najveci_broj



lista_brojeva = [12, 44, 91, 66, 1, 123, 52, 214, 410, 6, 22, 100]
print(f"Broj sa najvecom armstrongovom sumom iz liste {lista_brojeva} je {najveca_armstrongova_suma(lista_brojeva)}.")