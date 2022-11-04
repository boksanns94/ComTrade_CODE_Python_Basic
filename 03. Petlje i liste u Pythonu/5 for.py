# for petlja 
# osnovna funkcija for petlje jeste da je to petlja 
# sa nekim brojacem 
# taj brojac u svakom prolasku uzima razlicitu vrednost i odradjuje 
# telo petlje sa tom vrednosti
# for naziv_promenljive in range(x,y,z)
# x - predstavlja pocetnu vrednost brojaca, koja je ukljucena u opseg
# y - predstavlja krajnju vrednost brojaca, koja NIJE UKLJUCENA u opseg
# z - predstavlja korak za koliko se svaki put uveca "naziv_promenljive"
# nakon ponavljanja tela petlje 
# for i in range(x,y,z):
    # komande koje se ponavljaju 
    # za razlicite vrednosti i 
    # u opsegu od x do y, sa korakom z
# ispis brojeva od 1 do 10
for i in range(1,11,1):
    print(i,end=" ")
    
print()
# brojevi od 11 do -1 sa korakom 2
# 11 9 7 5 3 1 -1
for i in range(11,-2,-2):
    print(i,end=" ")
    
print()
# for petlja sa 2 argumenta u rangeu
# for i in range(x,y) 
# z podrazumevano 1
for i in range(1,11):
    print(i,end=" ")
# 3. varijanta for petlje sa rangeom je da range ima jedan argumenta
# for i in range(y) 
# z-> podrazumevano 1
# x-> podrazumevano 0
print()
for i in range(5): # i uzima sve vrednosti od 0 do y-1
# takodje ova petlja se ponavlja tacno "y" puta 
    print(i,end=" ")
    
#print(list(range(1,11)))
    