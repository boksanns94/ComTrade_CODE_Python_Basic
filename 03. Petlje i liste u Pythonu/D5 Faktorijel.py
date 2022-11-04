# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:51:15 2021

@author: Boksan
"""

broj = int(input("Unesite broj: "))

while broj <= 0:
    print("Pogresan unos! Unesite ponovo.")
    broj = int(input("Unesite broj: "))


print("\nStampa preko FOR petlje:")
faktorijel = 1
for i in range(1,broj+1):
    faktorijel = faktorijel * i
    
print(f"Faktorijel broja {broj} je {faktorijel}.")


print("\nStampa preko WHILE petlje:")
i = broj
faktorijel = 1
while i != 0:
    faktorijel = faktorijel * i
    i = i - 1

print(f"Faktorijel broja {broj} je {faktorijel}.")