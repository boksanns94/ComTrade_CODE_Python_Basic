# Korisnik unosi elemente liste, sve dok ne unese neki negativan broj. 
# Kada se prekine unos liste, ispisati sve elemente liste 
# a zatim izracunati proizvod elemenata liste koji su na parnoj poziciji.

# 3 4 5 1 2 -1 
# -> [3,4,5,1,2] 

brojevi = [] # lista je na pocetku prazna 

# unos = int(input("Unesite neki broj:")) # unesemo neki element  -1 
# while unos >= 0: # sve dok je taj element veci ili jednak 0 
    # brojevi.append(unos) # unesemo ga u listu
    # unos = int(input("Unesite neki broj:")) # trazimo novi unos 
# print(brojevi)

while True:
    unos = int(input("Unesite neki broj:"))
    if unos < 0:
        break # prekidamo petlju uz pomoc break-a 
    brojevi.append(unos)
print(brojevi)

# proizvod elemenata na parnim pozicijama 
# kada trazimo proizvod -> imacemo neku promenljivu koja ce cuvati rezultat 
proizvod = 1 # zasto na 1, pa 1 ne utice na rezultat mnozenja 
brojac = 0 # brojac treba za slucaj da ne postoji nijedan takav element, jer ako je brojac ostao 0, to znaci da nema proizvoda.  ( nece biti 1 ) 
# elementi na parnim pozicijama u listi 
# treba da prodjemo kroz listu koriscenjem pozicija, for i in range..
n = len(brojevi)
for i in range(n): # i uzima vrednosti od 0 do n-1 
# sto su ujedno i pozicije u nasoj listi, -> svaki element ce biti brojevi[i] 
# i=0 brojevi[0] i=1 brojevi[1] 
    if i % 2 == 0:
        print(brojevi[i],end=" ")
        proizvod = proizvod * brojevi[i]
        brojac = brojac + 1 
if brojac != 0:
    print("Proizvod elemenata na parnim pozicijama je:",proizvod)
else:
    print("Nema nijedan takav element")

# 2. nacin 
proizvod = 1
for i in range(0,n,2):
    proizvod = proizvod * brojevi[i]
print(proizvod)
# proizvod = 1
# for broj in brojevi:
    # pozicija_elementa = brojevi.index(broj) # index je metoda koja nam vraca poziciju te vrednosti u listi,ali PRVO POJAVLJIVANJE
    # if pozicija_elementa % 2 == 0: # ovo radi samo u slucaju da je lista sacinjena od jedinstvenih elemenata, bez ponavljanja
        # proizvod = proizvod * broj
# print(proizvod)

# 3. nacin 
print(brojevi[::2])
proizvod = 1 
parne_pozicije = brojevi[::2]
for broj in parne_pozicije:
    proizvod = proizvod * broj
print(proizvod)

# 4) Algoritam za trazenje minimuma i maksimuma u listi.
# ispisati najveci element u listi 

# a = 10
# b = 5 
# c = 6 
# d =  8
# trenutni_maks = a 
# if b > trenutni_maks:
    # trenutni_maks = b
# if c > trenutni_maks:
    # trenutni_maks = c
# if d > trenutni_maks:
    # trenutni_maks = d
# print(trenutni_maks)
trenutni_maks = brojevi[0] # trenutni maksimum postavimo na prvi element iz liste 
# na ovaj nacin smo se osigurali da je maksimum neki od elemenata iz liste 
for broj in brojevi: # prodjemo kroz sve elemente u listi 
    if broj > trenutni_maks: # pitamo da li je trenutni broj veci od trenutnog maksimuma
        print(f"Maksimum je bio {trenutni_maks}, ali je {broj} veci od njega i on postaje novi maks")
        trenutni_maks = broj # ako jeste menjamo trenutni maksimum, na taj broj
# moze i preko for i in range(n) -> if brojevi[i] > trenutni_maks -> trenutni_maks = brojevi[i]

print("Najveci element liste:",trenutni_maks)
# pozicija najmanjeg elementa ? 
n = len(brojevi)
trenutni_min = brojevi[0] # proglasim prvi element za trenutno najmanji
trenutna_pozicija_minimuma = 0
for i in range(n): # i ide od 0 do n-1 -> sto su ujedno i pozicije u listi =-> brojevi[i] -> element te liste unutar petlje
    if brojevi[i] < trenutni_min:
        trenutni_min = brojevi[i]
        trenutna_pozicija_minimuma = i # element koji je brojevi[i] je novi minimum, brojevi[i] -> "i-ti" element niza, odnosno njegova pozicija je i
print("Najmanji element liste je:",trenutni_min) 
print("Pozicija minimuma:",trenutna_pozicija_minimuma)
