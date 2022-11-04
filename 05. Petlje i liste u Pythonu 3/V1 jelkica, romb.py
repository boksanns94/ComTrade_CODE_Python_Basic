# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 20:27:06 2021

@author: Boksan
"""

# korisnik unos n, napraviti date sablone

n = int(input("Unesite n: "))
while n < 1:
    n = int(input("Greska. Ponovo: "))

# jelkica:
# n = 3   <- bitni su redovi, 3 reda
#   *
#  ***
# *****

for i in range(n):
    print(f"{(2*i+1) * '*':^{2*n+1}}")

# romb:
# n = 3   <- bitni su redovi, 3 reda do sredine
#   *
#  ***
# *****
#  ***
#   *

<<<<<<< HEAD
for i in range(n):
    print(i,end="")
    print(f"{(2*i+1) * '*':^{2*n+1}}")
for i in range(n-2,-1,-1):
    print(i,end="")
    print(f"{(2*i+1) * '*':^{2*n+1}}")
=======
>>>>>>> main
