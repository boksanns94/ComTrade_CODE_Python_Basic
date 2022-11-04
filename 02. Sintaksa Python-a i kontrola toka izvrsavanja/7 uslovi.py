# Korisnik unosi brojilac i imenilac razlomka, ispisati koliki je kolicnik

brojilac = int(input("Unesite brojilac:"))
imenilac = int(input("Unesite imenilac:"))

# if USLOV:
    # komande koje se desavaju
    # ako je uslov tacan 
# else:
    # komande koje se desavaju ako
    # uslov NIJE TACAN

# CTRL + Q komentarise red
    
if imenilac != 0: 
    kolicnik = brojilac/imenilac
    print(f"{brojilac} / {imenilac} = {kolicnik}")

if imenilac == 0:
    print("Los unos imenioca, ne sme biti 0!")

# selektujete redove 
# shift + tab uvlaci redove nazad
# tab - gura redove napred
    
if imenilac == 0:
    # ako zelite da ostavite prazan blok, morate da iskoristite
    # kljucnu rec pass 
    # pass je komanda koja ne radi nista, vec samo postuje pajtonovu
    # sintaksnu normu da mora postojati jedna komanda u bloku
    print("Los unos imenioca, ne sme biti 0!")
    #pass
else: 
    kolicnik = brojilac/imenilac
    print(f"{brojilac} / {imenilac} = {kolicnik}")
print("Kraj zadatka") # vracamo se 1 tab "unazad" da bismo nastavili
# dalje redom sa komandama