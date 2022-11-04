
brojevi = [3,4,5,12,13,3,3,3]

# metode listi -> one predstavljaju funkcije koje su svojstvene samo za elemente koji su tipa liste 

# sve liste imaju svoje metode za dodavanje novih elemenata 
# append 
# naziv_promenljive.naziv_metode(argumenti,arg1,arg2)
print(brojevi)
brojevi.append(10) # append je funkcija koja dodaje neku vrednost na kraj liste kao novi element
print(brojevi)
# insert -> insert je metoda koja prima dva argumenta
# 1. argument predstavlja poziciju na koju se ubacuje element
# 2. argument predstavlja vrednost koja se ubacuje na tu poziciju
brojevi.insert(3,100)
print(brojevi)

# extend -> koja kao argument prima neku drugu listu i sve elemente te liste pojedinacno ubacuje u samu listu
druga_lista = [11,42,33]
brojevi.extend(druga_lista)
print(brojevi)

# kako bismo bez extenda, dodali sve elemente iz druge liste u listu brojevi na kraj?
# brojevi.append(druga_lista)
# print(brojevi)
for broj in druga_lista: # broj ce uzimati redom vrednosti iz druge liste pocevsi od pozicije 0 do kraja liste
    brojevi.append(broj)  # i svaki od tih elemenata ja zelim da dodam na kraj liste 
    print(brojevi)
duzina_druge_liste = len(druga_lista)
for i in range(duzina_druge_liste): # pozicije u listi uzimaju vrednosti od 0 do duzina liste - 1 
# for i in range(n) -> i ce uzimati vrednosti od 0 do n-1 -> tacno pozicije koje ce uzimati elementi u listi 
    brojevi.append(druga_lista[i]) # naziv_liste[i] -> za element u listi koji se nalazi na "i"
    print(brojevi)
# append dodaje tacno 1 element na kraj liste bio on lista, konkretan broj string ili nesto drugo
# extend dodaje svaki element neke liste pojedinacno, u nasu listu 
brojevi.append(druga_lista)
print(brojevi)

#-----------------------------------------------------------------------------------------------------------
# Metode za izbacivanje elemenata iz liste:
brojevi.pop()  # pop je metoda listi, koja izbacuje poslednji element iz liste u slucaju da ne primi nista kao argument
print(brojevi)
brojevi.pop(3) # ako pop primi argument on izbacuje element sa TE POZICIJE U LISTI!
print(brojevi)
#brojevi.pop(1000)# ako izbacujemo element iz liste i pozicija koju smo prosledili nije validna -> list index out of range error

brojevi.remove(3) # remove izbacuje neku vrednost iz liste, u slucaju da ta vrednost postoji u listi, ali izbacuje SAMO PRVO POJAVLJIVANJE TOG BROJA U LISTI
print(brojevi)

ponavljanja_trojke = brojevi.count(3) # brojevi.count(neka_vrednost) broji koliko puta se argument ponavlja u listi 
print(ponavljanja_trojke)
# kako bismo izbacili sve trojke 
# petlja treba da se ponavlja onoliko puta koliko ima trojki u listi, i svaki put brisemo jednu trojku iz liste.
for _ in range(ponavljanja_trojke): # ova promenljiva i nam sluzi kao iterator 
# for i in range(3) -> i ce uzimati vrednosti 0,1,2 
    brojevi.remove(3) 
print(brojevi)
    
# in - je koriscen vec u for petlji -> for promenljiva in lista -> 
# ako se in koristi u uslovu -> tada on proverava da li je neka vrednost u listi 
# if 51 in brojevi:
    # print("51 je u listi")
# else:
    # print("51 nije u listi")
# kako bih izbacio sve 11-ice iz liste 
print()
while 11 in brojevi:
    brojevi.remove(11)
print(brojevi)

# brojevi.clear() # clear izbacuje sve elemente iz liste
# print(brojevi)
#---------------------------------------------------------------------------------------------------


lista_gradova = ["beograd","BEOGRAD","nis","lazarevac","krusevac","palic"]
lista_gradova.sort() # svaki karakter na tastaturi ima svoju odgovarajucu vrednost u ascii tabeli 
print(lista_gradova)
print(ord('a')) # ord -> koja prima neki karakter  i vraca nam koja je vrednost tog karaktera u UNICODE  tabeli
print(ord('A'))
print("Brojevi pre sortiranja:",brojevi)
# sortiranje elemenata liste 
# sortiranje je dovodjenje liste u neki redosled od najmanjeg/najveceg do najveceg/najmanjeg elementa 
brojevi.sort(reverse = True) # brojevi.sort() -> menja listu brojevi i sortira je od najmanjeg do najveceg elementa i kao rezultat izvrsavanja ne vraca nista ( None ) 
# reverse je opcioni argument .sort i sorted koji nam oznacava da li je sortirana lista oid najmanjeg ka najvecem ili od najveceg ka najmanjem
print(brojevi)
#print(brojevi.sort(reverse=True))
brojevi = sorted(brojevi)
#print(sorted(brojevi)) # sorted je funkcija koja prima neku listu kao argument i kao rezultat vraca novu listu koja je sortirana,poziv ove funkcije NE MENJA DIREKTNO LISTU BROJEVI
# VEC ON PRAVI NOVU LISTU
print(brojevi)
brojevi = sorted(brojevi,reverse=True)
print(brojevi)


# sortirana_lista = sorted(brojevi)
# print(sortirana_lista)

# x = 5
# x.sort()

pozicija_prve_13 = brojevi.index(13) # index je metoda koja nam vraca POZICIJU PRVOG pojavljivanja nekog broja u listi 
print(pozicija_prve_13)
# ako trazite index od nekog broja koji ne postoji u listi, program ce puci i reci ce number not in list 
# .reverse je metoda koja okrece listu unazad, tj radi isto sto i brojevi[::-1]
brojevi = [3,4,12,3]
print(brojevi)
print(brojevi[::-1])
print(brojevi)
brojevi.reverse()
# brojevi = brojevi[::-1]
print(brojevi)





    

