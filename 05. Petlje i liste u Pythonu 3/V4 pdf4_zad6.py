# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:16:50 2021

@author: Boksan
"""

# korisnik unosi broj n, program iscrtava
# zvezdice u n*n sablonu

n = int(input("Unesite n: "))
while n < 1:
    n = int(input("Greska. Ponovo: "))

# =============================================================================
# for i in range(n):
#     for j in range(n):
#         print("*", end="")
#     print()
# =============================================================================

for i in range(n): # bolje resenje od gornjeg
    print(n * "*")