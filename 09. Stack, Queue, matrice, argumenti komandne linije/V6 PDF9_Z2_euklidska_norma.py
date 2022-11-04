from sys import argv

if len(argv) != 3:
    print("Pogresan unos! Unesite tacno 3 elementa: ime dokumenta, broj redova i broj kolona matrice.")
    exit()

redovi = int(argv[1])
if redovi <= 0 or redovi > 50:
    print("Pogresan unos broja redova! Ponovo.")
    exit()

kolone = int(argv[2])
if kolone <= 0 or kolone > 50:
    print("Pogresan broj kolona! Ponovo.")

matrica = []
print("Unesite elemente matrice: ")
for i in range(redovi):
    print(f"Unesite elemente {i+1}. reda matrice:")
    trenutni_red = []
    for j in range(kolone):
        unos = int(input(f"Unesite element [{i}][{j}]: "))
        trenutni_red.append(unos)
    print(f"Zavrsili smo unos {i+1}. reda matrice: {trenutni_red}")
    matrica.append(trenutni_red)

zbir = 0
for i in range(redovi):
    for j in range(kolone):
        zbir += pow(matrica[i][j],2)
norma = zbir**(0.5)

print("Matrica:")
for i in range(redovi):
    for j in range(kolone):
        print(matrica[i][j],end=" ")
    print()
print(f"Euklidska norma matrice je: {norma:.3f}.")