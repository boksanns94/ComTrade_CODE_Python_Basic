# korisnik unosi dva broja, ispisati ko ima veci prosek i koliki je taj prosek
# napraviti funkciju prosek cifara, koja ce kao argument da primi neki broj
# i da vrati kao rezultat prosek 
def prosek_cifara(broj): 
    suma = 0
    brojac = 0 # za prosek nam trebaju suma i brojac 
    while broj > 0: # sve dok je broj veci od 0
        poslednja_cifra = broj % 10 # izdvajamo cifru
        broj = broj // 10 # skracujemo broj za jednu cifru
        suma = suma + poslednja_cifra # uvecavamo sumu za tu poslednju cifru
        brojac = brojac + 1 # brojac za 1 
    
    prosek = suma / brojac 
    return prosek 
    
def prosek_cifara_ispis(broj): 
    suma = 0
    brojac = 0 # za prosek nam trebaju suma i brojac 
    while broj > 0: # sve dok je broj veci od 0
        poslednja_cifra = broj % 10 # izdvajamo cifru
        broj = broj // 10 # skracujemo broj za jednu cifru
        suma = suma + poslednja_cifra # uvecavamo sumu za tu poslednju cifru
        brojac = brojac + 1 # brojac za 1 
    
    prosek = suma / brojac 
    print("Prosek je",prosek) 
    
prvi = int(input("Unesite prvi broj:"))
drugi = int(input("Unesite drugi broj:"))

prosek1 = prosek_cifara(prvi)
prosek2 = prosek_cifara(drugi)

print(prosek1,prosek2)

import math # da biste koristili neki modul treba da ga "uvezete"
# import naziv_modula 

print(math.sqrt(25))
import pymongo

#ADD A,A,B
#a = a+b 
    