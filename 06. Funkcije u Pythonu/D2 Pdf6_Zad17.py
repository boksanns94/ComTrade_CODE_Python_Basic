# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:29:15 2021

@author: Boksan
"""

# iscrtati romb

def iscrtaj_razmake(n):
    print(n*" ",end="")

def iscrtaj_zvezdice(n):
    print(n*"*",end="")

def iscrtaj_romb(n):
    for i in range(n,0,-1):
        iscrtaj_razmake(i-1)
        iscrtaj_zvezdice(n)
        print()


n = int(input("Unesi broj: "))
while n <= 0:
    n = int(input("Greska. Ponovo: "))
iscrtaj_romb(n)
