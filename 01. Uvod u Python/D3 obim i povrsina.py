# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 20:20:51 2021

@author: Boksan
"""

#Domaci zadatak #3
# Korisnik unosi poluprecnik na standardni ulaz.
# Izracunati povrsinu i obim kruga sa zadatim poluprecnikom.

r = float(input("Unesite poluprecnik u mm: "))
print("\n")

print(f"Obim kruga:  {2*r*3.14:<.2f} mm")
print(f"Povrsina kruga:  {r**2*3.14:<.2f} mm2")