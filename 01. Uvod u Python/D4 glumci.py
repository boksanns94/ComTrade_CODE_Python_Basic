# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:31:04 2021

@author: Boksan
"""

#Domaci zadatak #4
# Dozvoliti korisniku da unese ime omiljenog filma, godinu kada je snimljen
# film, glavnog glumca tog filma, imdb ocenu tog filma. Nakon toga je
# potrebno da odgovarajuce poruke ispisete uz pomoc printa, koriscenjem
# vise argumenata u printu i koriscenjem konkatenacije stringova.

ime_filma = input("Unesite ime vaseg omiljenog filma: ")
godina_snimanja = input("Unesite godinu kada je snimljen: ")
ime_glavnog_glumca = input("Unesite ime glavnog glumca: ")
imdb_ocena = input("Unesite imdb ocenu tog filma: ")

print("\n\nPrva varijanta:", end = "\n")
print("Vas omiljeni film je", ime_filma)
print("Film je snimljen", godina_snimanja, "godine.")
print("Glavni glumac je", ime_glavnog_glumca)
print("Na IMDB ovaj film ima ocenu:", imdb_ocena)

print("\n\nDruga varijanta:", end = "\n")
print("Vas omiljeni film je " + ime_filma)
print("Film je snimljen " + godina_snimanja + " godine.")
print("Glavni glumac je " + ime_glavnog_glumca)
print("Na IMDB ovaj film ima ocenu: " + imdb_ocena)

print("\n\nTreca varijanta:", end = "\n")
print("Vas omiljeni film je " + ime_filma + ", i snimljen" \
      " je " + godina_snimanja + " godine. Njegov glavni glumac" \
      " je " + ime_glavnog_glumca + " i na IMDBu je dobio" \
      " ocenu: " + imdb_ocena + ".")