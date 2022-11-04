# PDF9 - Zadatak 5
#
# Napisati program koji predstavlja simulaciju igre “vešala”. Kao argumenti
# komandne linije učitavaju se reč i maksimalan broj pokušaja. Nakon toga korisnik
# pogađa slova, ukoliko potroši maksimalan broj pokušaja izgubio je igru, ako
# pogodi pre nego što je iskoristio maksimalan broj pokušaja dobio je igru. Ispisati
# poruku o ishodu igre.
#
# Primer unosa: py hangman.py rec 4

from sys import argv

if len(argv) != 3:
    print("Pogresan unos argumenata. Unesite ime fajla, rec za pogadjanje i broj pokusaja.")
    exit()

tajna_rec = argv[1]
br_pokusaja = int(argv[2])
if br_pokusaja < 1:
    print("Pogresan unos argumenata. Broj pokusaja mora biti barem 1.")
    exit()

pogresni_pokusaji = [] # za cuvanje pogresnih pokusaja
trenutno_pogadjanje = ['_' for i in range(len(tajna_rec))] # za cuvanje tacnih pogodaka
pobeda = False # za ispitivanje da li je rec cela pogodjena

print()
print()
while br_pokusaja != 0:
    print(f"Broj preostalih gresaka: {br_pokusaja}") # stampa br preostalih pokusaja

    print("Pogresni pokusaji: ", end=" ") # stampa svih prethodnih slova koji nisu u reci
    for j in range(len(pogresni_pokusaji)):
        print(pogresni_pokusaji[j],end=" ")

    print()
    print("Rec koja se pogadja: ", end=" ") # stampa trenutnog stanja reci koja se pogadja
    for j in range(len(trenutno_pogadjanje)):
        print(trenutno_pogadjanje[j],end=" ")

    print()
    pokusaj = input("Unesite slovo: ") # unos pokusaja pogadjanja slova
    if pokusaj in tajna_rec:                    # ako je dobar pogodak
        pozicija = tajna_rec.find(pokusaj)      # trazim index tog slova u reci
        trenutno_pogadjanje[pozicija] = pokusaj # stavljam ga na istu poziciju u listi za trenutno pogadjanje
        print("Dobar pogodak!!!")
    else:                                       # ako nije dobar pogodak
        pogresni_pokusaji.append(pokusaj)       # smestam je u listu pogresnih pogodaka
        br_pokusaja -= 1                        # i smanjujem br preostalih pogodaka
        print("Steta... Pokusaj ponovo...")

    if "_" not in trenutno_pogadjanje:  # provera da li je rec vec pogodjena bez da su se istrosili pokusaji
        pobeda = True
        break                           # ako jeste pogodjena, izlazim iz petlje

    print()
    print()

if pobeda:
    print("ODLICNO! POGODIO SI CELU REC!")
else:
    print("Alaaa si ga obesio....")