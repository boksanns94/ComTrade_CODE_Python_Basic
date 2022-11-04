# liste se deklarisu sa uglastim zagradama
#           0           1       2           3       4           5
voce = ["pomorandza","jabuka","tresnja","visnja","breskva","mango"]
#           -6          -5      -4          -3      -2          -1
print(voce)
# svaki element liste, tj njegova vrednost 
# je odredjena sa nazivom liste i pozicijom(index-om) u listi
# pozicije u listama krecu od 0!!!!
# pristup pojedinacnom elementu ->  
# naziv_liste[pozicija]
print(voce[1])
#print(voce[23])
broj_elemenata_liste = len(voce) # len je funkcija koja 
# kao argument prima neku listu ili kolekciju,
# i kao rezultat vraca broj elemenata u toj listi
print("Lista ima",broj_elemenata_liste,"elemenata")
#Pozicije u listi su vrednosti od 
# 0 do len(lista) - 1 
print("Poslednji element liste:",voce[broj_elemenata_liste-1])
# python podrzava negativno indeksiranje
print("Poslednji element liste:",voce[-1])

# Slajsovanje listi 
# predstavlja nacin kako cemo da ispisemo samo deo liste, tj
# da izdvojimo deo liste u novu listu
# naziv_liste[x:y:z]
# x - pocetna poziciju od koje izdvajamo koja je ukljucena u opseg
# y - krajnja pozicija koja NIJE ukljucena u opseg
# z - je korak za koliko se pozicija pomera
#print(voce[x:y:z])
voce = ["pomorandza","jabuka","tresnja","visnja","breskva","mango"]
print(voce[1:4:2])
print(voce[-1:1:-1]) # ako zelimo da se krecemo kroz listu unazad
# krecemo od "vece" pozicije,tj "vise desne" pozicije u listi
# do pozicije unazad sa negativnim korakom
print(voce[5:1:-1])

print(voce[2:4]) 
# ako se ne navede treca vrednost za korak, korak je podrazumevano 1
print(voce[:3]) # ako ostavite prvo mesto prazno
# isto kao print(voce[0:3])
# on ce biti pocetak liste
print(voce[3:]) # ako se izostavi krajnji index,onda cemo ici do kraja 
#liste
# 0. i 3.
#print(voce[3:len(voce)]
print(voce[0:4:3])
#print(voce[2,3])
#range[1,10]
print(voce[::])
print(voce[::-1])
print(voce[:2:-1])
# ako je korak negativan, onda je pocetak podrazumevano kraj liste
print(voce[::-2])
#           0123456789
recenica = "Danas je cetvrtak"
print(recenica[2:7])
palindrom = "anavolimilovana"
if palindrom == palindrom[::-1]:
    print("Jeste palindrom")
else:
    print("Nije palindrom")
    
mesovita_lista = ["Test",True,None,123,-123.5]
print(mesovita_lista)

# s = {
    # "ime" : "Dusan",
    # "prezime" : "Sijacic",
    # "prosek" : 123
# }
# print(s["ime"]) za kasnije u kursu