# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 22:06:41 2021

@author: Boksan
"""

n = int(input("Unesite n: "))
while n < 1:
    n = int(input("Greska. Ponovo: "))

for i in range(n): # stampa gornje polovine masne, bez srednjeg reda
    print(f"{i*'*':<{n}}",end="") # stampa leve polovine reda
    print(f"{i*'*':>{n}}") # stampa desne polovine reda
    
print(n*2*'*') # stampa srednjeg reda

for i in range(n-1,-1,-1): # stampa donje polovine masne, posle srednjeg reda
    print(f"{i*'*':<{n}}",end="") # stampa leve polovine reda
    print(f"{i*'*':>{n}}") # stampa desne polovine reda