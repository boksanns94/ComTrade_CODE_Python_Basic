# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 21:08:11 2021

@author: Boksan
"""

# napisati funkciju koja prima broj i vraca broj cifara tog broja

def broj_cifara(broj):
    if broj < 0:            # za negativne brojeve
        broj *= -1
    return len(str(broj))



broj = int(input("Unesite broj: "))
print(broj_cifara(broj))