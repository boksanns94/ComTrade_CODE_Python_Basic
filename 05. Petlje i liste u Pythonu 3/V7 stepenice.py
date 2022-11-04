# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:41:12 2021

@author: Boksan
"""

# korisnik unos n, napraviti stepenice od 1 do n od *

n = int(input("Unesite n: "))
while n < 1:
    n = int(input("Greska. Ponovo: "))

# 1.
# n = 3
# *
# **
# ***

print("1.")
for i in range(n):
    print(f"{ (i+1) * '*'}")

# 2.
# n = 3
#   *
#  **
# ***

print("2.")
for i in range(n):
    print(f"{ (i+1) * '*' :>{n}s}")

# 3.
# n = 3
# ***
#  **
#   *

print("3.")
for i in range(n,0,-1):
    print(f"{i * '*' :>{n}s}")

# 4.
# n = 3
# ***
# **
# *

print("4.")
for i in range(n,0,-1):
    print(f"{i * '*'}")