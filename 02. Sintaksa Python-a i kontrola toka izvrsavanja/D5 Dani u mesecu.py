# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:27:34 2021

@author: Boksan
"""

#Domaci zadatak 5
# Napisati program koji za unetu godinu i mesec ispisuje naziv meseca
# kao i koliko dana ima u tom mesecu. U slucaju loseg unosa, ispisati gresku.

godina = int(input("Unesite redni broj godine: "))
mesec = int(input("Unesite redni broj meseca: "))

if mesec == 1:
    print("Januar, 31 dan.")
elif mesec == 2:
    if godina % 400 == 0:
        print("Februar, 29 dana.")
    elif godina % 100 == 0:
        print("Februar, 28 dana.")
    elif godina % 4 == 0:
        print("Februar, 29 dana.")
    else:
        print("Februar, 28 dana.")
elif mesec == 3:
    print("Mart, 31 dan.")
elif mesec == 4:
    print("April, 30 dana.")
elif mesec == 5:
    print("Maj, 31 dan.")
elif mesec == 6:
    print("Jun, 30 dana.")
elif mesec == 7:
    print("Jul, 31 dan.")
elif mesec == 8:
    print("Avgust, 31 dan.")
elif mesec == 9:
    print("Septembar, 30 dana.")
elif mesec == 10:
    print("Oktobar, 31 dan.")
elif mesec == 11:
    print("Novembar, 30 dana.")
elif mesec == 12:
    print("Decembar, 31 dan.")