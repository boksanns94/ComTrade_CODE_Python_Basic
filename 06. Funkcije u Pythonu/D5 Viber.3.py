# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 22:17:28 2021

@author: Boksan
"""

def broj_cifara(broj):
    if broj < 0:            # ako korisnik unese negativan broj
        broj *= -1
    return len(str(broj))

def armstrongova_suma(broj):
    armstrongova_suma = 0
    for cifra in str(broj):
        if cifra == "-":    # ako korisnik unese negativan broj
            continue
        armstrongova_suma += int(cifra)**broj_cifara(broj)
    return armstrongova_suma

def da_li_je_armstrongov_broj(broj):
    if broj < 0:            # ako korisnik unese negativan broj
        broj *= -1
    if broj == armstrongova_suma(broj):
        return True
    else:
        return False



broj = int(input("Unesite broj: "))
if da_li_je_armstrongov_broj(broj):
    print(f"Broj {broj} jeste armstrongov broj.")
else:
    print(f"Broj {broj} nije armstrongov broj.")