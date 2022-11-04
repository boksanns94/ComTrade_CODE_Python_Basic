# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:12:13 2021

@author: Boksan
"""

broj = int(input("Unesite broj: "))
temp = broj

if broj != 0:
    while temp % 10 == 0:
        temp = temp // 10

print(f"Broj {broj} bez nula sa desne strane je {temp}.")