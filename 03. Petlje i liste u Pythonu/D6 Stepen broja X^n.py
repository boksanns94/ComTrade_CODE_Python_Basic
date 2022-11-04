# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 18:01:03 2021

@author: Boksan
"""

osnova_stepena = float(input("Unesite osnovu stepena: "))
izlozilac = int(input("Unesite izlozilac: "))

while izlozilac < 0:
    print("Neispravan unos izlozioca. Mora biti ceo i nenegativan broj.")
    izlozilac = int(input("Unesite izlozilac: "))

rezultat = osnova_stepena
for i in range(2,izlozilac+1):
    rezultat = rezultat * osnova_stepena


if izlozilac == 0 and osnova_stepena != 0:
    print(f"Rezultat stepenovanja {osnova_stepena} na {izlozilac} je 1.0.")
else:
    print(f"Rezultat stepenovanja {osnova_stepena} na {izlozilac} je {rezultat}.")