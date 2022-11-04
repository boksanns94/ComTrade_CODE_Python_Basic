# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 20:36:59 2021

@author: Boksan
"""

#Zadatak 1
# Ispisati 5 puta "Mi volimo da programiramo."
for i in range(5):
    print(f"{i+1}. Mi volimo da programiramo.")
    
#Zadatak 2
# Korisnik unosi koliko puta zeli da ispise tekst
# Ispisati toliko puta "Mi volimo da programiramo."
while True:
    n = int(input("Unesite broj ponavljanja: "))
    if n <= 0:
        print("Mora biti pozitivan broj!")
        continue
    break

for i in range(n):
    print(f"{i+1}. Mi volimo da programiramo.")

#while a < 2:
#    ovaj blok