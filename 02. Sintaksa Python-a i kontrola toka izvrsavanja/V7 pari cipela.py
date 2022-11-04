# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 20:35:50 2021

@author: Boksan
"""

#korisnik unosi koliko pari cipela zeli da kupi
#ako kupi 1-9 cena je 12$
#ako kupi 10-100 cena je 10$
#ako kupi 100+ cena je 7$
#ispisati total na kraju

pari_cipela = int(input("Koliko pari cipela: "))

if pari_cipela <= 0:
    print("Nista ga ne kosta!")
    exit()
elif pari_cipela < 10:
    print(f"{pari_cipela} pari cipela ga kosta {12*pari_cipela}$")
elif pari_cipela < 100:
    print(f"{pari_cipela} pari cipela ga kosta {10*pari_cipela}$")
else:
    print(f"{pari_cipela} pari cipela ga kosta {7*pari_cipela}$")