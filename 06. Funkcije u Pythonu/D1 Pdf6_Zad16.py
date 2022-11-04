# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 17:33:36 2021

@author: Boksan
"""

# napisati funkciju par_nepar(n) koja ispituje da li su cifre datog
# celog broja, naizmenicno parne pa neparne

def da_li_je_cifra_parna(cifra):
    if cifra % 2 == 0:
        return True
    else:
        return False

def da_li_je_cifra_neparna(cifra):
    if cifra % 2 != 0:
        return True
    else:
        return False

def da_li_broj_ispunjava_uslov(broj):
    for i in range(len(broj)):
        if i % 2 == 0:
            if not da_li_je_cifra_parna(int(broj[i])):
                return False
        if i % 2 != 0:
            if not da_li_je_cifra_neparna(int(broj[i])):
                return False
    return True



broj = input("Unesite broj: ")
while int(broj) <= 0:
    broj = input("Greska. Ponovo: ")
    
if da_li_broj_ispunjava_uslov(broj):
    print("Broj ispunjava uslov.")
else:
    print("Broj ne ispunjava uslov.")
