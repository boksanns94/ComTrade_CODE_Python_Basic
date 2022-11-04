# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 21:24:52 2021

@author: Boksan
"""

pozitivan_flag = 0
proizvod = 1

uneti_brojevi = [int(input("Unesite broj: "))]

while True:
    if uneti_brojevi[-1] == 0:
        break
    uneti_brojevi.append(int(input("Unesite broj: ")))

if len(uneti_brojevi) == 1:
    print("Nije unet ni jedan broj!")
else:
    for i in range(len(uneti_brojevi)):
        if uneti_brojevi[i] > 0:
            proizvod = proizvod * uneti_brojevi[i]
            pozitivan_flag = 1
    if pozitivan_flag == 0:
        print("Medju unetim brojevima nema pozitivnih!")
    else:
        print(f"Proizvod pozitivnih brojeva je {proizvod}.")