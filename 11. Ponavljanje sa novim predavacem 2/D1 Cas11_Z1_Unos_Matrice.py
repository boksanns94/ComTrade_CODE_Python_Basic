from sys import argv

if len(argv) != 3: # ispitivanje da li je unet dovoljan broj argumenata
    print("Unesite tacno 3 argumenta! Naziv python fajla, broj redova i broj kolona.")
    exit()

m = int(argv[1]) # preuzimanje zadatog broja redova sa argumenta
if m < 1 or m > 5: # ispitivanje da li je dobro unet broj redova
    print("Greska: Broj redova mora biti izmedju 1 i 5.")
    exit()
n = int(argv[2]) # preuzimanje zadatog broja kolona sa argumenta
if n < 1 or n > 5: # ispitivanje da li je dobro unet broj redova
    print("Greska: Broj kolona mora biti izmedju 1 i 5.")
    exit()

matrica = [] # prazna matrica
print("Unesite elemente matrice: ")
for i in range(m): # unos redova matrice
    print(f"Unesite elemente {i+1}. reda matrice:")
    trenutni_red = [] # pravljenje praznog reda kao privremenu listu
    for j in range(n): # unos kolona u svakom od redova
        unos = input(f"Unesite element [{i}][{j}]: ")
        trenutni_red.append(unos) # dodavanje elemenata u trenutnom redu
    print(f"Zavrsili smo unos {i+1}. reda matrice: {trenutni_red}") 
    matrica.append(trenutni_red) # kada je popunjen red, dodajemo ga u matricu

for i in range(m): # ispis matrice
    for j in range(n): # ispis jednog reda
        print(matrica[i][j],end=" ") # ispis svih elemenata u redu
    print() # prelazak u novi red pre ispisa sledeceg reda, kako bi lepse izgledao ispis