# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 21:11:09 2021

@author: Boksan
"""

# napisati funkciju koja racuna armstrongovu sumu
# armstrongova suma je zbir svih cifara stepenovanih na broj cifara

def broj_cifara(broj):
    if broj < 0:            # podrska za negativne brojeve
        broj *= -1
    return len(str(broj))

def armstrongova_suma(broj):
    suma = 0
    for cifra in str(broj):
        if cifra == "-":    # podrska za negativne brojeve
            continue
        suma += int(cifra)**broj_cifara(broj)
    return suma



broj = int(input("Unesite broj: "))
print(f"Armstrongova suma broja {broj} je {armstrongova_suma(broj)}.")