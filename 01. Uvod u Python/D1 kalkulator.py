# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:07:07 2021

@author: Boksan
"""

#Domaci zadatak #1
# Napisati program koji emulira jako prost kalkulator.
# Korisnik unosi dva broja na standardnom ulazu, a program ispisuje rezultat
# sabiranja, oduzimanja, mnozenja i deljenja uneta dva broja.

n1 = int(input("Unesite prvi broj (b1): "))
n2 = int(input("Unesite drugi broj (b2): "))
print("\n")

print("Sabiranje (b1 + b2): ", n1 + n2)
print("Oduzimanje (b1 - b2): ", n1 - n2)
print("Mnozenje (b1 * b2): ", n1 * n2)
print("Celobrojno deljenje (b1 // b2): ", n1 // n2)
print("Decimalno deljenje (b1 / b2): ", n1 / n2)
print("Ostatak (b1 % b2): ", n1 % n2)