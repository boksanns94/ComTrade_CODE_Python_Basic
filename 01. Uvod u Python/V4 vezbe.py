# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 20:33:50 2021

@author: Boksan
"""

# ispisati tekst
text = input("Poruka:")
print(text)

# uneti broj i ispisati kvadratnu vrednost tog broja
broj = int(input("Unesite broj:"))
print(broj**2)

# zadatak 1
# korisnik unosi poluprecnik
# izracunati povrsinu i obim
r = float(input("Unesite poluprecnik: "))
print("Obim kruga: ", 2*r*3.14)
print("Povrsina kruga: ", r**2*3.14)

# zadatak 2
# Korisnik unosi sekunde
# konvertovati te sekunde u format hh:mm:ss ili ##min ##sec
time = int(input("Unesite sekunde: "))
sek = time % 60
minut = ((time - sek) // 60) % 60
cas = (time - sek) // 3600
print(cas,":",minut,":",sek)