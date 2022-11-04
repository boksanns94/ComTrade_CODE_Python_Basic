from sys import argv
def unesi_kvadratnu_matricu(n):
    matrica = []
    for i in range(n): # za svaki od n redova 
        trenutni_red = [] # pravimo listu za svaki red
        for j in range(n): # za svaki red prolazimo kroz sve kolone 
            unos = int(input("Unesite element matrice:"))
            trenutni_red.append(unos)
        # kada se zavrsi unutrasnja petlja 
        # u matricu dodajemo taj red
        matrica.append(trenutni_red)
    return matrica
def ispisi_kvadratnu_matricu(matrica):
    for red in matrica:
        for element in red:
            print(element,end=" ")
        print()

if len(argv) != 2:
    print("Unesite tacno 2 argumenta, naziv fajla i dimenziju kvadratne matrice!")
    exit()
n = int(argv[1]) # zato sto je argv lista stringova -> moramo da je konvertujemo u int 
if n<1 or n>50:
    print("Losa dimenzija matrice!")
    exit()

matrica = unesi_kvadratnu_matricu(n)
ispisi_kvadratnu_matricu(matrica)

# kako da proverimo da li je neka lista sortirana ? 
def da_li_je_sortirana(lista_brojeva):
    # da bi lista bila sortirana neopadajuce ( od manjih ka vecem )
    # 0 1 2 3 4 5 6
    # 3 6 6 7 8 9 9
    #  i     i-1
    # [1] >= [0]
    # [2] >= [1]
    # [3] >= [2]
    # [4] >= [3]
    # [5] >= [4]
    # [6] >= [5]
    for i in range(1,len(lista_brojeva)):
        if lista_brojeva[i] < lista_brojeva[i-1]:
            return False # ako se makar jednom desi da je element iza veci od trenutnog onda ta lista nije rastuca 
    return True
brojevi = [1,1,2,3,4,5]
print(da_li_je_sortirana(brojevi))
# ij ij ij
# 00 01 02 
# 10 11 12
# 20 21 22 
# -> elementi na dijagonali -> 00 11 22  (glavna dijagonala)   -> i = j 
# -> elementi na sporednoj dijagonali -> 02 11 20 ( sporedna dijagonala ) i + j = n - 1 

glavna = []
sporedna = [] 
sve_kolone = []
for i in range(n):
    trenutna_kolona = []
    for j in range(n):
        if i==j:
            glavna.append(matrica[i][j])
        if i+j == n-1:
            sporedna.append(matrica[i][j])
        trenutna_kolona.append(matrica[j][i])
    sve_kolone.append(trenutna_kolona)

print(glavna)
print(sporedna)
print(sve_kolone)


