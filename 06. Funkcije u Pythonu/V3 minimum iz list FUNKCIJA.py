# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 18:50:44 2021

@author: Boksan
"""

# napisati funkciju koja kao argument prima listu brojeva i kao rezultat vraca najveci broj u listi
def maksimum_u_listi(spisak):
    najveci = spisak[0]
    for broj in spisak:
        if najveci < broj:
            najveci = broj
    return najveci

spisak_brojeva = [1,6,2,4,89,3,1,3,66,33,6,7,223,5,73,22]
print(maksimum_u_listi(spisak_brojeva))
