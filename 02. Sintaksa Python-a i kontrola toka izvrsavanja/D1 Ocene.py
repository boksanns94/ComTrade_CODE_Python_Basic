# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:46:11 2021

@author: Boksan
"""

#Domaci zadatak 1
# Profesor unosi broj poena sa ispita.
# Program treba da proveri da li je student polozio ispit 
# i da ispise sa kojom ocenom
# 0-50 - 5
# 51-60 - 6
# 61-70 - 7
# 71-80 - 8
# 81-90 - 9
# 91-100 - 10

broj_poena = int(input("Unesite broj poena:"))

if broj_poena < 0 or broj_poena > 100:
    print("Los unos, broj poena mora biti od 0 do 100")
elif broj_poena < 51:
    print("Nema ocenu.")
elif broj_poena < 61:
    print("Ocena 6.")
elif broj_poena < 71:
    print("Ocena 7.")
elif broj_poena < 81:
    print("Ocena 8.")
elif broj_poena < 91:
    print("Ocena 9.")
else:
    print("Ocena 10.")