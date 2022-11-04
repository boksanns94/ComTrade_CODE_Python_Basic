# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:39:24 2021

@author: Boksan
"""

# 1. formiranje liste
# korisnik unosi n, i onda unosi po jedan element dok ih ne bude n komada

n = int(input("Unesite duzinu liste: "))
brojevi = []
for i in range(n):
    unos = int(input(f"Unesite {n+1}. element liste: "))
    brojevi.append(unos)
print(brojevi)


# 2. zbir svih elemenata liste

trenutni_zbir = 0
for i in range(n):
    trenutni_zbir = trenutni_zbir + brojevi[i]
print(f"Zbir elemenata liste je {trenutni_zbir}.")

#zbir parnih vrednosti elemenata liste
trenutni_zbir_parnih = 0
for i in range(n):
    if brojevi[i] % 2 == 0:
        trenutni_zbir_parnih = trenutni_zbir_parnih + brojevi[i]
print(f"Zbir parnih elemenata liste je {trenutni_zbir_parnih}.")


# 3. brojanje desavanja u listi

brojac = 0
for broj in brojevi:
    if broj > brojevi[1]:
        brojac = brojac + 1
print(f"Brojac je na kraju: {brojac}")


# 4. Prosek vrednosti elemenata liste

zbir_elemenata = 0
broj_elemenata = 0

for broj in brojevi:
    zbir_elemenata = zbir_elemenata + broj
    broj_elemenata = broj_elemenata + 1

prosek = zbir_elemenata + broj_elemenata
print(f"Prosek vrednosti elemenata liste je {prosek}.")


# 5. Unos dok se ne unese negativan broj

brojevi = []
while True:
    unos = int(input("Unesite elemenat liste: "))
    if unos < 0:
        break
    brojevi.append(unos)
print(brojevi)

# 6. Proizvod elemenata na parnim pozicijama

# 1. nacin
n = len(brojevi)
proizvod = 1
for i in range(n):
    if i % 2 == 0:
        proizvod = proizvod * brojevi[i]
        brojac = brojac + 1
if brojac != 0:
    print(f"Proizvod elemenata na parnim pozicijama je {proizvod}")

# 2. nacin
proizvod = 1
for i in range(0,n,2):
    proizvod = proizvod * brojevi[i]
print(f"Proizvod elemenata na parnim pozicijama je {proizvod}")

# 3. nacin, najvise u duhu pythona
parne_pozicije = brojevi[::2]
proizvod = 1
for broj in parne_pozicije:
    proizvod = proizvod * broj
print(f"Proizvod elemenata na parnim pozicijama je {proizvod}")


# 7. algoritam za trazenje max i min
# max
trenutni_max = brojevi[0]
for broj in brojevi:
    if broj > trenutni_max:
        trenutni_max = broj
print(trenutni_max)
# min
trenutni_min = brojevi[0]
for broj in brojevi:
    if broj < trenutni_min:
        trenutni_min = broj
print(trenutni_min)


# 8. trazenje pozicije min i max elementa
# min
trenutni_min = brojevi[0]
pozicija_trenutnog_min = 0
for broj in brojevi:
    if broj < trenutni_min:
        trenutni_min = broj
        pozicija_trenutnog_min = i
print(trenutni_min)
print(pozicija_trenutnog_min)
# max
trenutni_max = brojevi[0]
pozicija_trenutnog_max = 0
for broj in brojevi:
    if broj < trenutni_max:
        trenutni_max = broj
        pozicija_trenutnog_max = i
print(trenutni_max)
print(pozicija_trenutnog_max)