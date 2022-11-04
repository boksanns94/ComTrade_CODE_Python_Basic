from sys import argv

if len(argv) != 2:
    print("Pogresan unos! Unesite tacno 2 elementa: ime dokumenta, dimenziju matrice.")
    exit()

redovi = int(argv[1])
if redovi <= 0 or redovi > 50:
    print("Pogresan unos broja redova! Ponovo.")
    exit()
kolone = redovi

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

# da li su sortirane po redovima
sort_red = True
for i in range(redovi):
    for j in range(kolone-1):
        if matrica[i][j] > matrica[i][j+1]:
            sort_red = False

# da li su sortirane po kolonama
sort_kol = True
for i in range(kolone):
    for j in range(redovi-1):
        if matrica[i][j] > matrica[i][j+1]:
            sort_kol = False

# da li su sortirane dijagonale
sort_dijag = True
for i in range(redovi-1):
    if matrica[i][-i-1] > matrica[i+1][-(i+1)-1]:
        sort_dijag = False
    if matrica[i][i] > matrica[i+1][i+1]:
        sort_dijag = False

print("Matrica:")
for i in range(redovi):
    for j in range(kolone):
        print(matrica[i][j],end=" ")
    print()

if sort_red:
    print("Elementi jesu strogo rastuci po redovima.")
else:
    print("Elementi nisu strogo rastuci po redovima.")

if sort_kol:
    print("Elementi jesu strogo rastuci po redovima.")
else:
    print("Elementi nisu strogo rastuci po kolonama.")

if sort_dijag:
    print("Elementi jesu strogo rastuci po dijagonalama.")
else:
    print("Elementi nisu strogo rastuci po dijagonalama.")