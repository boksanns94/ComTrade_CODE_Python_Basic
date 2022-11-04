# kada bi u izrazu za zagrade postojale sve tri vrste zagrada?
# ([{}])
# (])

def push(lista_za_stek,element_koji_dodajemo):
    if len(lista_za_stek) < 10: # ako je manji od maksimalnog kapaciteta steka
        lista_za_stek.append(element_koji_dodajemo)
        return True
    print("Ne mozemo da dodamo element na stack, stack je pun! STACKOVERFLOW")
    return False
# pop osim sto izbacuje element iz steka, on i vraca tu vrednost poslednjeg elementa
def pop(lista_za_stek):
    if len(lista_za_stek) == 0:
        print("Ne mozemo da izbacimo element sa praznog stack-a! STACKUNDERFLOW")
        return None
    poslednji = lista_za_stek.pop() # pop vraca poslednji element i izbacuje ga iz liste
    return poslednji # vracamo taj poslednji element 

def zagrade_konacno(unos_sa_zagradama):
    stek = [] 
    #                   0   1   2
    lista_otvorenih = ['(','[','{'] # u obe liste na istim pozicijama se nalaze zagrade koje zatvaraju jedna drugu
    lista_zatvorenih = [')',']','}']
    # 2 - {}
    # 1 - []
    # 0 - ()
    # ([{])
    # stek = [  (       ]
    # stek = [  (,[     ]
    # stek = [  (,[,{   ]
    for karakter in unos_sa_zagradama: # prolazimo karakter po karater
        #print(stek)
        if karakter in lista_otvorenih: # ako je karakter medju otvorenim zagradama dodajemo ga na stek
            push(stek,karakter) # poslednja otvorena zagrada je poslednji element na steku
        elif karakter in lista_zatvorenih: # ako je zagrada zatvorena
            # to znaci da treba da izbacimo element sa steka
            zagrada_koja_treba_da_zatvori_trenutnu = pop(stek) # popujemo element sa steka
            # i ako je taj element jednak None to znaci da je stek bio prazan
            # da nije bio prazan vratio bi nam neku zagradu
            if zagrada_koja_treba_da_zatvori_trenutnu == None:
                return False # slucaj da ima vise zatvorenih zagrada nego otvorenih zagrada u nekom trenutku
            # poslednji element steka nam predstavlja zagradu koja treba da zatvori trenutni karakter ( a taj trenutni 
            # # karaakter je jedna od zatvorenih zagrada ),] ili } )

            # da bi one mogle da zatvore jedna drugu -> one MORAJU DA BUDU NA ISTOJ POZICIJI u listi otvorenih i u listi zatvorenih
            #print(zagrada_koja_treba_da_zatvori_trenutnu,karakter)
            pozicija_otvorene = lista_otvorenih.index(zagrada_koja_treba_da_zatvori_trenutnu) # dohvatimo poziciju otvorene
            # zagrade iz liste otvorenih 
            pozicija_zatvorene = lista_zatvorenih.index(karakter) # dohvatimo poziciju iz liste zatvorenih za zatvorenu
           # print(pozicija_otvorene,pozicija_zatvorene)
            if pozicija_zatvorene != pozicija_otvorene: # ako su one razlicite 
                print(karakter,"ne moze da zatvori",zagrada_koja_treba_da_zatvori_trenutnu)
                return False # onda imamo slucaj da je neka zagrada pogresno zatvorena sa drugom vrstom zagrade
    #print("Stek na kraju:",stek)
    if len(stek) == 0: # ako je stek ostao prazan, to znaci da su sve zagrade zatvorene kako treba 
        return True
    else:
        return False # ako nije 0, to je znak da ima vise otvorenih nego zatvorenih zagrada

print("*")
test_unos = "([{}])" # dobre zagrade
print(zagrade_konacno(test_unos))


test_unos = "([{)])" # pogresna zagrada je zatvorila ) 
print(zagrade_konacno(test_unos))

test_unos = "([])}" # imamo vise zatvorenih zagrada u nekom trenutku
print(zagrade_konacno(test_unos))
test_unos = "([{}])    ({" # vise otvorenih zagrada na kraju
print(zagrade_konacno(test_unos))

