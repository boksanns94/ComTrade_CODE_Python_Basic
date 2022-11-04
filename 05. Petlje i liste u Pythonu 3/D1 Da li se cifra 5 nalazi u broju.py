# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 22:38:08 2021

@author: Boksan
"""

flag_5 = 0
broj = int(input("Unesite broj: "))

while broj % 10 != 0:
    if broj % 10 == 5:
        flag_5 = 1
    broj = broj // 10

if flag_5 == 1:
    print("Uneti broj sadrzi cifru 5.")
else:
    print("Uneti broj ne sadrzi cifru 5.")