# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:35:47 2021

@author: Boksan
"""

#stampanje vrednosti promenljive
#promenljive se koriste bez navodnika
ime = "Milos"
print(ime)

#pisanje teksta zajedno sa vrednostima promenljivih
print("Moje ime je   ", ime)

#unos podataka komandom input
ime = input("Unesite ime:")
print(ime)

#unos broja komandom input
broj = input("Unesite omiljeni broj:")
print("Vas omiljeni broj je: ", broj)
print(broj * 4)

#castovanje int broja
broj = int(broj)
print(broj * 4)
broj = broj * 10

#castovanje decimalnog broja
decimalni = input("Unesite neki broj:")
decimalni = float(decimalni)
print(decimalni)

# n = 20
# print("Podatak je" + n) # ovde ce se napraviti greska
# print("Podatak je", n) # ovde se nece napraviti greska