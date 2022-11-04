# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:22:16 2021

@author: Boksan
"""

#Domaci zadatak 4
# Napisati program koji za uneti redni broj dana u nedelji ispisuje ime
# tog dana. U slučaju neispravnog unosa, ispisati gresku.

redni_br_dana = int(input("Unesite redni broj dana: "))

if redni_br_dana < 1 or redni_br_dana > 7:
    print("Pogresan unos! Broj mora biti od 1 do 7.")
elif redni_br_dana == 1:
    print("Dan je ponedeljak.")
elif redni_br_dana == 2:
    print("Dan je utorak.")
elif redni_br_dana == 3:
    print("Dan je sreda.")
elif redni_br_dana == 4:
    print("Dan je cetvrtak.")
elif redni_br_dana == 5:
    print("Dan je petak.")
elif redni_br_dana == 6:
    print("Dan je subota.")
else:
    print("Dan je nedelja.")