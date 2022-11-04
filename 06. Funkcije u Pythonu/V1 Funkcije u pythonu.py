# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 17:25:12 2021

@author: Boksan
"""

# deklaracija funkcija:
# def ime_funkcije(argumenti):
#   telo_funkcije

def pozdravi():
    print("Hello World")

# pozivanje funkcije
# vrsi se pisanjem imena funkcije i njenim argumentima

print("Komande pre funkcije")
pozdravi()
print("Komanda posle funkcije")

# funkcija sa argumentom
def pozdravi_me(ime):
    print(f"Hello {ime}.")
    print(moje_prezime)
moje_prezime = "Boksan"
pozdravi_me("Milos")
pozdravi_me(moje_prezime)

# funkcije koje vracaju vrednost
def promeni(x):
    x = x + 1
    return x # da bi funkcija vratila vrednost mora da ima return
a = 2
a = promeni(a)
print(a) # a ce u prethodnom redu postati 3

# Ako zelimo direktno da menjamo promenljivu, koristimo rezervisanu rec global
def promeni_zaista():
    global a # ovo a i a u 42. redu se odnose na istu promenljivu
    a = a + 1
a = 2 # a u 40. redu i ovo a se odnose na istu promenljivu
promeni_zaista() # funkcija u sebi zna koja je promenljiva a bez da se prosledjuje