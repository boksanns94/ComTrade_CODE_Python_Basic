# unos podataka pomocu inputa

# pojam promenljive 
# Promenljiva predstavlja imenovanu memorijsku lokaciju
# koja cuva neku vrednost 
# naziv promenljive moze biti sastavljen
# od malih, velikih slova, cifara i znaka _
 

ime = "Milan" # 
# operator = -> predstavlja operator za DODELU VREDNOSTI 
# on radi tako sto se desna strana jednakosti 
# izracuna i onda se vrednost upise u odgovarajucu 
# promenljivu sa leve strane

print(ime) # prilikom ispisa promenljive 
# naziv promenljive se ispisuje BEZ NAVODNIKA

# svi nazivi u pythonu su CASE SENSITIVE  
# mala slova i velika slova nisu ISTO!
# moje ime je ______ ( vrednost promenljive ime ) 
print("Moje ime je: ", ime)
ime="Dusan"
print("ime")
# input je funkcija koja kao argument prima neku poruku
# koju cemo poslati samom korisniku pre nego sto mu trazimo neki unos
# i taj tekst koji je korisnik uneo, je rezultat funkcije input

ime = input("Unesite vase ime: ")
print("Moje ime je:", ime)

broj = input("Unesite vas omiljeni broj:")
print("Vas omiljeni broj je", broj) 
# Python1.2020

print(broj * 3)

# rezultat funkcije poziva funkcije input je tekstualni podatak

