# korisnik unosi dva broja, pocetni i krajnji 
# ispisati svaki drugi broj pocevsi od manjeg do veceg.

# pocetni -> 4
# krajnji -> 10
# 4 6 8 10
# pocetni -> 10
# krajnji -> 4
# 4 6 8 10
pocetni = int(input("Unesite pocetni broj:"))
krajnji = int(input("Unesite krajnji broj:"))
korak = 2
#if pocetni > krajnji: # ako je pocetni veci od krajnjeg
# samo im zamenimo vrednosti 
    # pomocna = pocetni
    # pocetni = krajnji
    # krajnji = pomocna
    #pocetni,krajnji = krajnji,pocetni
    #korak = -korak
if pocetni > krajnji:
    pocetni,krajnji = krajnji,pocetni
#print(pocetni,krajnji)
for i in range(pocetni,krajnji+1,korak):
    print(i,end=" ")