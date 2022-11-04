# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:59:27 2021

@author: Boksan
"""

#Domaci zadatak 2

# Slajd 18:
# Uneti ceo broj i ispitati da li je paran. Ispisati poruku.
# Koristiti samo if petlju

broj = int(input("Unesite broj: "))

if broj % 2 == 0:
    print(f"Broj {broj} je paran.")
if broj % 2 != 0:
    print(f"Broj {broj} je neparan.")

# Slajd 19:
# Uneti ceo broj i ispitati da li je paran. Ispisati poruku.
# Koristiti if-else petlju

broj = int(input("Unesite broj: "))

if broj % 2 == 0:
    print(f"Broj {broj} je paran.")
else:
    print(f"Broj {broj} je neparan.")

# Slajd 20:
# Uneti broj sa standardnog ulaza i proveriti da li je uneti broj
# manji od 100, veci od 100 a manji od 200 ili veci od 200 a manji od 300
# ili veci od 300. Ispisati odgovarajucu poruku.

broj = int(input("Unesite broj: "))

if broj < 100:
    print(f"Broj {broj} je manji od 100.")
elif broj == 100:
    print(f"Broj {broj} je 100.")
elif broj < 200:
    print(f"Broj {broj} je veci od 100 a manji od 200.")
elif broj == 200:
    print(f"Broj {broj} je 200.")
elif broj < 300:
    print(f"Broj {broj} je veci od 200 a manji od 300.")
else:
    print(f"Broj {broj} je ili 300 ili je veci od 300.")