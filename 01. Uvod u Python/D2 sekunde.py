# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 20:11:32 2021

@author: Boksan
"""

#Domaci zadatak #2
# Napisati program koji pretvara sekunde u minute i sate.
# Korisnik unosi broj na standardnom ulazu, a program ispisuje rezultat
# na standardnom izlazu. Rezultat treba da bude u formatu: 11h 22m 33s

broj = int(input("Unesite broj sekundi:"))

sekunde = broj % 60
minuti = (broj // 60) % 60
sati = broj // 3600

print(f"{sati}h {minuti}m {sekunde}s") 