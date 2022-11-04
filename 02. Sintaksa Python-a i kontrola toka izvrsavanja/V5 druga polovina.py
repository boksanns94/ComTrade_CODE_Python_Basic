# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 19:33:42 2021

@author: Boksan
"""

# korisnik unosi brojilac i imenilac razlomka, ispisati koliki je kolicnik
brojilac = int(input("Unesite brojilac: "))
imenilac = int(input("Unesite imenilac: "))

#kolicnik = brojilac / imenilac
#print(f"{brojilac} / {imenilac} = {kolicnik}")

#ako korisnik unese 0 kao imenilac program ce da izbaci gresku



if imenilac != 0:
    kolicnik = brojilac / imenilac
    print(f"{brojilac} / {imenilac} = {kolicnik}")

if imenilac == 0:
    print("Imenilac ne sme biti 0!")




if imenilac == 0:
    print("Imenilac ne sme biti 0!")
else:
    kolicnik = brojilac / imenilac
    print(f"{brojilac} / {imenilac} = {kolicnik}")



# rezervisana rec PASS
if imenilac != 0:
    pass
else:
    pass # ne radi nista






# korisnik unosi neku ocenu
# ako korisnik unese 1 pise se nedovoljan 1
# ako unese 2 pise se dovoljan 2, i tako za sve ocene

ocena = int(input("Unesite ocenu: "))
if ocena == 1:
    print("Nedovoljan 1!")
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
                    print("Los unos ocene!")
                    
                    

# ovaj kod i prethodni rade identicnu stvar
if ocena == 1:
    print("Nedovoljan 1")
elif ocena == 2:
    print("Dovoljan 2")
elif ocena == 3:
    print("Dobar 3")
elif ocena == 4:
    print("Vrlo dobar 4")
elif ocena == 5:
    print("Odlican 5")
else:
    print("Los unos ocene!")
    





# profesor unosi broj poena sa ispita
# proveriti da li je student polozio ispit i sa kojom ocenom
# 0-50 - 5
# 51-60 - 6
# 61-70 - 7
# 71-80 - 8
# 81-90 - 9
# 91-100 - 10

broj_poena = int(input("Unesite broj poena:"))

if broj_poena < 0 or broj_poena > 100:
    print("Los unos, broj poena mora biti od 0 do 100")
elif broj_poena >= 0 and broj_poena < 51:
    print("Nema ocenu.")
elif broj_poena >= 51 and broj_poena < 61:
    print("Ocena 6.")
elif broj_poena >= 61 and broj_poena < 71:
    print("Ocena 7.")
elif broj_poena >= 71 and broj_poena < 81:
    print("Ocena 8.")
elif broj_poena >= 81 and broj_poena < 91:
    print("Ocena 9.")
elif broj_poena >= 91:
    print("Ocena 10.")