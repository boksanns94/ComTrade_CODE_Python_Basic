# prolazak kroz listu 
#           0           1       2           3       4           5
voce = ["pomorandza","jabuka","tresnja","visnja","breskva","mango","kiwi","papaja","lubenica"]
#           -6          -5      -4          -3      -2          -1

# print(voce[0],end=" ")
# print(voce[1],end=" ")
# print(voce[2],end=" ")
# print(voce[3],end=" ")
# print(voce[4],end=" ")
# print(voce[5],end=" ")
# print()
# 1) prolazak kroz listu preko pozicija
duzina = len(voce)
for i in range(duzina):
# i=0 -> ja zelim da ispisem voce[0]
# i=1 -> ja zelim da ispisem voce[1]
# i=2 -> ja zelim da ispisem voce[2]
# i = x -> ja zelim da ispisem voce[x]
    print(f"Element na poziciji {i} je {voce[i]}")
    #kada range prima samo jedan argument
    # i uzima sve vrednosti od 0 do taj broj - 1 ( duzina - 1)
    # sto su ujedno i sve pozicije u listi te duzine
for i in range(duzina):
    print(voce[i],end=" ")
    # pristupamo svim elementima sa naziv_liste[i] 
print()
voce = ["pomorandza","jabuka","tresnja","visnja","breskva","mango","kiwi","papaja","lubenica"]
# 2) prolazak kroz listu preko neke privremene promenljive u for petlji
for vocka in voce: # for promenljiva in naziv_liste(moze i slajsovanje)
# promenljiva vocka u svakom prolasku kroz petlju uzima vrednosti 
# redom iz liste voce pocevsi od pozicije 0 pa do kraja liste
    print(vocka,end=" ")
print(vocka)    
# for(i=0;i<10;i=i+1)
# {
    # printf("%d ",i); 
# }
# -> 0 1 2 3 4 5 6 7 8 9
print()
for i in range(1,10,2):
    print(i,end=" ")
print()
print(list(range(1,10,2)))
print()
brojevi = [3,5,3,2,1]
for broj in brojevi:
    print(broj,end=" ")