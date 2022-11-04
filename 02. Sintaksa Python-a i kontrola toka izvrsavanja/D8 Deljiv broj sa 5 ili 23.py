# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 16:30:01 2021

@author: Boksan
"""

broj = int(input("Unesite neki broj: "))

if broj % 5 == 0 or broj % 23 == 0:
    print(f"Broj {broj} je deljiv sa 5 ili sa 23.")
else:
    print(f"Broj {broj} nije deljiv ni sa 5, ni sa 23.")