from sys import argv

# Napisati program koji učitava i zatim ispisuje elemente učitane matrice. Kao
# argumenti komandne linije učitavaju se dva cela broja m i n (tim redosledom), a
# potom i elementi matrice celih brojeva dimenzije m × n. Pretpostaviti da je
# maksimalna dimenzija matrice 50x50, u slučaju neispravnog unosa ispisati
# odgovarajuću poruku o grešci.
print(argv)
if len(argv) != 3:
    print("Unesite tacno 3 argumenta naziv pajton fajla, broj redova i broj kolona u matrici!!!")
    exit()

m = int(argv[1]) # broj_redova matrice 
n = int(argv[2]) # broj_kolona 
print(m,n)
if m<1 or m>50 or n<1 or n>50:
    print("Los unos dimenzije matrice!")
    exit()

matrica = [] 
# za svaki red u matrici ja moram da napravim listu elemenata 
for i in range(m): # i uzima sve vrednosti od 0 do m-1 
    # svaki put kada fiksiramo i -> tada unosimo elemente koji se nalaze u i-tom redu
    print(f"Unesite elemente iz {i+1}. reda:")
    trenutni_red = []
    for j in range(n): # prolazimo kroz sve kolone 
        unos = int(input(f"Unesite broj iz {i+1}. reda i {j+1}.kolone:")) # trazimo unose 
        trenutni_red.append(unos) # dodajemo u trenutni red 
    print(f"Zavrsili smo popunjavanje {i+1}. reda matrice!",trenutni_red) # kada se zavrsi petlja napravljen je jedan red
    # tj podlista matrice 
    matrica.append(trenutni_red) # dodajemo u matricu
    print(matrica)
# zad 2 racunanje euklidske norme 
suma_za_euklida = 0 # racunamo sumu suma je na pocetku nula 
for red in matrica:
    for element in red:
        print(element,end= " ")
        suma_za_euklida += element**2 # svaki put sumu uvecamo za kvadrat 
    print()
print(suma_za_euklida)
from math import sqrt # u modulu math postoji metoda sqrt koja vraca koren nekog broja
print("euklidska norma:",sqrt(suma_za_euklida))
print("euklidska norma:",suma_za_euklida**(0.5))


