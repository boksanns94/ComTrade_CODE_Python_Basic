# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:13:35 2021

@author: Boksan
"""

#Domaci zadatak 3
# Napisati program koji pomaze kasirki da obracuna kusur. Za unetu cenu,
# kolicinu i iznos, program treba da ispise kusur. Svi brojevi su celi i
# pozitivni. Pretpostaviti da je unos ispravan.

cena_artikla = int(input("Unesite cenu artikla: "))
kolicina_artikla = int(input("Unesite kolicinu kupljenog artikla: "))
uplacen_iznos = int(input("Unesite uplacen iznos: "))

print(f"\nKusur: {uplacen_iznos-cena_artikla*kolicina_artikla}")