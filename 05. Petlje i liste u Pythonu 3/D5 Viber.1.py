# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 22:31:44 2021

@author: Boksan
"""

n = int(input("Unesite n: "))
while n < 1:
    n = int(input("Greska. Ponovo: "))

brojevi = []
for i in range(n):
    brojevi.append(int(input(f"Unesite {i+1}. element: ")))

proizvod = 1
print("Brojevi: ",end="")
for i in range(n):
    print(brojevi[i],end=" ")
    if i % 2 != 0 and brojevi[i] % 3 == 0:
        proizvod *= brojevi[i]
        
print()
print(f"Proizvod je {proizvod}.")