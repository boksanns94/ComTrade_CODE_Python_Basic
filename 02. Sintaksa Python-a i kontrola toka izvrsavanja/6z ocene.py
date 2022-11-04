# korisnik unosi neku ocenu 1 do 5
# ispisati koja je to ocena -> 
# 1 -> Nedovoljan 1
# 2 -> Dovoljan 2
# 3 -> Dobar 3
# 4 -> Vrlo dobar 4
# 5 -> Odlican 5

ocena = int(input("Unesite ocenu:"))

if ocena == 1:
    print("Nedovoljan 1")
else:
    if ocena == 2:
        print("Dovoljan 2")
    else:
        if ocena == 3:
            print("Dobar 3")
        else:
            if ocena == 4:
                print("Vrlo dobar 4")
            else:
                if ocena == 5:
                    print("Odlican 5")
                else:
                    print("Los unos za ocenu, unesite broj od 1 do 5!!")

if ocena == 1:
    print("Nedovoljan 1") # ako je 1 -> ovo se desi
elif ocena == 2: # ako nije 1, pitaj da li je 2
    print("Dovoljan 2")
elif ocena == 3: # ako nije ni jedan ni 2, pitaj da li je 3
    print("Dobar 3")
elif ocena == 4: # ako nije nista prethodno pitaj da li je 4
    print("Vrlo dobar 4")
elif ocena == 5: # ako nije nista od prethodnog -> pitaj da li je 5
    print("Odlican 5")
else: # ako nije ni 1 ni 2 ni 3 ni 4 ni 5 -> nije ocena 
    print("Nije dobar unos, mora biti broj od 1 do 5")
                    
print("Nastavak koda...")
        