# PDF9 - Zadatak 4
#
# Kvadratna matrica je magični kvadrat ako su sume elemenata u svim vrstama i
# kolonama jednake. Napisati program koji proverava da li je data celobrojna
# kvadratna matrica (čija se dimenzija učitava kao argument komandne linije)
# magični kvadrat i ispisati odgovarajuću poruku na standardni izlaz. Pretpostaviti da
# je maksimalna dimenzija matrice 50 × 50. U slučaju neispravnog unosa, ispisati
# odgovarajuću poruku o grešci.

from sys import argv

if len(argv) != 2:
    print("Pogresan unos argumenata. Unesite ime fajla i dimenziju matrice.")
    exit()

dimenzija = int(argv[1])
if dimenzija < 1 or dimenzija > 50:
    print("Pogresan unos argumenata. Dimenzija mora biti od 1 do 50.")
    exit()

matrica = []
for i in range(dimenzija):
    trenutni_red = []
    print(f"{i+1}. red: ")
    for j in range(dimenzija):
        unos = int(input(f"Unesite [{i+1}][{j+1}] element: "))
        trenutni_red.append(unos)
    matrica.append(trenutni_red)



suma_redovi = []
suma_kolone = []

# suma svih redova
for i in range(dimenzija):
    suma = 0
    for j in range(dimenzija):
        suma += matrica[i][j]
    suma_redovi.append(suma)

# suma svih kolona
for i in range(dimenzija):
    suma = 0
    for j in range(dimenzija):
        suma += matrica[j][i]
    suma_kolone.append(suma)

# trazenje razlicite sume
jeste_magicni_kvadrat = True
for red in suma_redovi:
    for kol in suma_kolone:
        if red != kol:
            jeste_magicni_kvadrat = False
            break

print(suma_kolone,suma_redovi)


print()
for i in range(dimenzija):
    for j in range(dimenzija):
        print(matrica[i][j],end=" ")
    print()

if jeste_magicni_kvadrat:
    print("Uneta matrica predstavlja magicni kvadrat!")
else:
    print("Uneta matrica NE predstavlja magicni kvadrat!")