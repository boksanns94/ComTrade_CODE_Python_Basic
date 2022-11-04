# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 20:13:28 2021

@author: Boksan
"""

#Korisnik unosi dva cela broj
#Izracunati i ispisati lepo formatirano sve racunske operacije

prvi = int(input("Unesite prvi broj: "))
drugi = int(input("Unesite drugi broj: "))
print(prvi, drugi)
print(prvi + drugi)

#sabiranje
zbir = prvi + drugi
print(prvi, "+", drugi, "=", zbir)

#oduzimanje
razlika = prvi - drugi
print(prvi, "-", drugi, "=", razlika)

#mnozenje
proizvod = prvi * drugi
print(prvi, "*", drugi, "=", proizvod)

#vrste deljenja
#celobrojno, decimalno i ostatak
decimalno = prvi / drugi
celobrojno = prvi // drugi
ostatak = prvi % drugi
print(prvi, "/", drugi, "=", decimalno)
print(prvi, "//", drugi, "=", celobrojno)
print(prvi, "%", drugi, "=", ostatak)
print(prvi, "/", drugi, "=", celobrojno, "(", ostatak, ")")

#stepenovanje
print(2**10)