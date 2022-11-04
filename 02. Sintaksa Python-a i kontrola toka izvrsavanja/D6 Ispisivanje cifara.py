# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:45:47 2021

@author: Boksan
"""

#Domaci zadatak 6
# Napisati program koji za uneti trocifren broj ispisuje cifre.

broj = int(input("Unesite trocifren broj: "))

jedinice = broj % 10
desetice = broj // 10 % 10
stotine = broj // 100

print(f"Broj: {broj}")
print(f"Stotine: {stotine}, Desetice: {desetice}, Jedinice: {jedinice}")