# Korisnik unosi n, a zatim i n elemenata liste celih brojeva.
# 1) Izracunati prosek elemenata koji su veci od razlike poslednjeg i prvog elementa u listi.
# 2) Izracunati proizvod elemenata koji su manji od proseka dobijenih iz tacke 1

# n -> 6
# 3 6 7 1 2 5  ( unos liste preko petlje ) 
# Razlika -> 5 - 3 = 2  ( racunanje razlike poslednjeg i prvog elementa)
# za prosek nam trebaju zbir i brojac koliko ih ima 
# prodjemo kroz listu, nadjemo elemente koji ispunjavaju uslov i menjamo zbir i brojac 
# prosek elemenata koji su veci od te razlike -> 3 6 7 5 
# zbir vecih od razlike poslednjeg i prvog -> 21 
# brojac: 4 
# na kraju racunamo prosek i ispisujemo ga 
# prosek -> 21 / 4 = 5.25 

n = int(input("Unesite duzinu liste:"))
brojevi = [] # lista je na pocetku prazna 
for i in range(n): # petlja koja se ponavlja n puta
    unos = int(input("Unesite broj za listu:"))
    brojevi.append(unos)
print(brojevi)

zbir_za_prosek = 0
brojac_za_prosek = 0
# poslednji element u listi je na poziciji -1, tj n-1 
# a prvi element je na poziciji 0
razlika = brojevi[-1] - brojevi[0]
print("Razlika poslednjeg i prvog je:",razlika)

# nova_lista = brojevi.pop() # pop osim sto izbacuje element iz liste sa poslednje pozicije 
# pop vraca taj element koji je izbacio kao rezultat operacije 
# print(nova_lista)

for broj in brojevi: # prodjemo kroz celu listu 
    if broj > razlika: # pitamo da li trenutni element ispunjava uslov iz zadatka
        zbir_za_prosek = zbir_za_prosek + broj # ako ispunjava, menjamo zbir, uvecavamo ga za taj broj, zasto za broj
        # pa on je ispunio uslov 
        brojac_za_prosek = brojac_za_prosek + 1 # a brojac uvek uvecavamo za 1, svaki put kada broj ispuni uslov
prosek = zbir_za_prosek / brojac_za_prosek # kada se zavrsi petlja, racunamo prosek kao zbir/brojac 
print("Prosek:",prosek) # ispisujemo prosek

# 2) proizvod elemenata koji su manji od proseka dobijenog iz tacke 1 
proizvod = 1
for broj in brojevi: # prodjemo kroz celu listu
    if broj < prosek: # ako je broj manji od proseka
        proizvod = proizvod * broj  # promenimo proizvod
print("Proizvod:",proizvod) # stampamo proizvod







