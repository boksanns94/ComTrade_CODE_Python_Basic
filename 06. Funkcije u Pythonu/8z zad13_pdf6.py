# zad 13 pdf 6 

def min(x:int,y:int,z:int) -> int:
    trenutni_minimum = x 
    if y < trenutni_minimum:
        trenutni_minimum = y
    if z < trenutni_minimum:
        trenutni_minimum = z 
    return trenutni_minimum
    
    #return najmanji_od_ta_tri broja
najmanji = min(10,3,-4)
print("asd",end="" )
print(najmanji)

prvi_broj = int(input("Unesite broj:"))
drugi_broj = int(input("Unesite broj:"))
treci_broj = int(input("Unesite broj:"))

najmanji = min(prvi_broj,drugi_broj,treci_broj)
print(najmanji)
# napisati funkciju koja kao argument prima listu brojeva i kao rezultat vraca najveci broj u listi.
def maks(lista_brojeva):
    """
    
            ja sam opis funkcije 
    """
    najveci = lista_brojeva[0] # proglasimo prvi element ( prvi element iz liste, tj element na poziciji 0 za trenutno najveci)
    
    for broj in lista_brojeva: # prodjemo kroz celu listu
        if broj > najveci: # pitamo da li je neki broj u listi veci od najveceg
            najveci = broj # promenimo najveci na taj broj
     
    return najveci # kao rezultat funkcije vratimo taj najveci broj
    
brojevi=[1,2,4,1,2,444,22,3,111]
rez = maks(brojevi)
print(rez)
print(help(maks))
    
