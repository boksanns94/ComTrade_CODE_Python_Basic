# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:27:28 2021

@author: Boksan
"""

n = int(input("Unesite n: ")) # unos n
while n <= 0: # provera n
    n = int(input("Pogresan unos! Ponovo: "))
    
brojevi = []
for i in range(n): # unos svih brojeva
    brojevi.append(float(input("Unesite broj: ")))

brojac_promena = 0
for i in range(n-1):
    if brojevi[i] < 0 and brojevi[i+1] >= 0:
        brojac_promena = brojac_promena + 1
    elif brojevi[i] >= 0 and brojevi[i+1] < 0:
        brojac_promena = brojac_promena + 1

# sta ako je lista: [0, 0, 0, 0, 0], onda ovo nije dobro
# =============================================================================
# for i in range(n-1):
#     if brojevi[i] * brojevi[i+1] <= 0:
#         brojac_promena = brojac_promena + 1 
# =============================================================================
        
print(f"Broj promena je {brojac_promena}.")