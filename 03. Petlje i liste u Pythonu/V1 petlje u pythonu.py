# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 18:14:43 2021

@author: Boksan
"""

# prvi primer for petlje
for i in range(1,11,1):
    print(i, end=" ")


# korak moze biti negativan, u tom slucaju brojanje ide u nazad    
for i in range(11, -2, -2):
    print(i, end=" ")
    
    
# ako se Z izostavi, podrazumeva se da je 1
for i in range(1, 11):
    print(i, end=" ")
    
# ako range ima samo 1 argument, podrazumeva se da je taj argument Y
# X se podrazumeva da je 0, a Z se podrazumeva da je 1
for i in range(5):
    print(i, end=" ")
# ova petlja se ponavlja tacno y puta
    

# Zadatak 1
# korisnik unosi dva broja pocetni i krajnji , ispisati svaki drugi broj
# pocevsi od manjeg ka vecem
pocetni = int(input("Unesi 1 ceo broj: "))
krajnji = int(input("Unesi 2 ceo broj: "))

if krajnji < pocetni:
    pocetni, krajnji = krajnji, pocetni

for i in range(pocetni, krajnji+1, 2):
    print(f"{i}", end=" ")
    
    
    
# prvi primer while petlje
# ispisati sve neparne brojeve od 1 do 10
i = 1
while i < 10:
    print(i, end = " ")
    i = i + 2



# Zadatak 2
# korisnik unosi dva cela broja. ispisati njihov kolicnik
# ako je imenilac = 0, naterati korisnika da ispravno unese broj
    
prvi = int(input("Unesite brojilac: "))
drugi = int(input("Unesite imenilac: "))

while drugi == 0:
    print("Greska! Deljenje sa nulom.")
    drugi = int(input("Unesite imenilac ponovo: "))

print(f"{prvi}/{drugi}={prvi/drugi}")



# Zadatak 2 sa beskonacnom petljom

prvi = int(input("Unesite brojilac: "))

while True:
    drugi = int(input("Unesite imenilac: "))
    if drugi != 0: # provera da li je unesena nula
        break # ako nije 0, izlazak iz cele petlje
    else:
        print("Los unos! Ponovo!")
    
print(f"{prvi}/{drugi}={prvi/drugi}")   