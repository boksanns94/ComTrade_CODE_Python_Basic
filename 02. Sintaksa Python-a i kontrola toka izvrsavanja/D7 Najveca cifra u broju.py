# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 16:10:38 2021

@author: Boksan
"""

ispitivani_broj = int(input("Unesite zeljeni broj: "))

if ispitivani_broj < 0:
    temp = ispitivani_broj*(-1)
else:
    temp = ispitivani_broj
sledeca_cifra = 0
najveca_cifra = 0

while temp != 0:
    if najveca_cifra < sledeca_cifra:
        najveca_cifra = sledeca_cifra
    sledeca_cifra = temp % 10
    temp = temp // 10

print(f"Najveca cifra u broju {ispitivani_broj} je {najveca_cifra}")