# korisnik unosi neki broj, proveriti da li je taj broj deljiv sa sumom svojih cifara

broj = int(input("Unesite broj:"))
if broj < 0:
    broj = -broj
kopija_broja = broj # sacuvamo inicijalnu vrednost broja 
zbir = 0 # posto trazimo zbir, treba nam pomocna promenljiva
# koja je na pocetku jednaka 0 
while broj > 0: # uz pomoc izdvajanja cifara izracunamo 
    poslednja_cifra = broj % 10 # sumu svih cifara tog broja
    broj = broj // 10
    zbir = zbir + poslednja_cifra 
# kao posledica izdvajaanja cifara,sam broj ce na kraju while petlje
# biti 0. u nastavku koristicemo kopiju tog broja, koja ima inicijalnu vrednost
# promenljive broj
print("Zbir cifara broja",kopija_broja,"je",zbir)

if kopija_broja % zbir == 0:
    print("da")
else:
    print("ne")