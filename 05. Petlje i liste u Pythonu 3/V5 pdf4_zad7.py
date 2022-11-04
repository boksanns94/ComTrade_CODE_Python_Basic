# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:35:06 2021

@author: Boksan
"""

# korisnik unosi n, program ispisuje
# sledeci sablon za npr n = 4:
# ****
# *  *
# *  *
# ****

n = int(input("Unesite n: "))
while n < 1:
    n = int(input("Greska. Ponovo: "))

for i in range(n):
    if i == 0 or i == n-1:
        print(n * "*")
    else:
        print(f'*{(n-2)*" "}*')