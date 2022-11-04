
# napisati funkcije push i pop, pretpostaviti da je maksimalan broj elemenata na stacku 10
# mi cemo stack za sada implementirati samo kao jednnu obicnu listu 

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
    poslednji = lista_za_stek.pop()
    return poslednji
# l1 =[]
# print(l1.pop())
# stek = []
# for i in range(4):
#     push(stek,10)
#     push(stek,15)
#     push(stek,11)
#     print(stek)
# for i in range(11):
#     pop(stek)
#     print(stek)

# 1) Validan unos : (5+3) * ( 3 + 6 )
# 2) (5+3) * )(1+3) -> desilo se da imamo vise zatvorenih nego otvorenih zagrada u nekom trenutku
# 3) (5+3) * ( 3 + 6 )( -> nije dobar ima vise otvorenih na kraju
def da_li_su_dobre_zagrade(unos_sa_zagradama):
    brojac_otvorenih = 0
    brojac_zatvorenih = 0
    for karakter in unos_sa_zagradama:
        #print(karakter)
        if karakter == '(': # provera da li je otvorena
            brojac_otvorenih +=1 # uvecavamo brojac otvorenih
        elif karakter == ')': 
            brojac_zatvorenih +=1 # kada se promeni broj zatvorenih zagrada, u tom slucaju moramo da proverimo
            # da li je imamo vise zatvorenih ili otvorenih zagrada
            if brojac_zatvorenih > brojac_otvorenih: # ako je taj uslov tacan 
                #print("nisu dobre")
                return False # to znaci da zagrade nisu dobro uparene, te vracamo False
    
    #print(brojac_otvorenih,brojac_zatvorenih)
    if brojac_otvorenih == brojac_zatvorenih: # na kraju proveravamo da li je konacan broj otvorenih i zatvorenih zagrada jednak
        #print("jesu dobre")
        return True
    else:
        #print("nisu dobre")
        return False
    #return brojac_zatvorenih == brojac_otvorenih
    

def zagrade_sa_stekom(stek,unos_sa_zagradama):
    # ( 2 + 3 ) - (3 + 4 )(
    # stek = [] 
    # -> naletimo na otvorenu zagradu -> [(]
    # -> naletimo na zatvorenu zagradu -> []
    # -> naletimo na otvorenu zagradu -> [(]
    # -> naletimo na zatvorenu zagradu -> [] 
    # -> naletimo na otvorenu zagradu -> [(]


    # )
    # [] 
    # naletim nazatvorenu -> posto je stek prazan desava se stack underflow, funkcija pop nam vraca None 
    for karakter in unos_sa_zagradama:
        if karakter == "(":
            push(stek,karakter)
        elif karakter == ")":
            prom = pop(stek) # pop vraca None ako je stek prazan,ako nije prazan vraca poslednji element sa stacka
            if prom == None:
                return False
    if len(stek) == 0:
        return True
    return False



stek = [] 
# kada naletimo na otvorenu zagradu -> ubacimo je na stek
# kada naletimo na zatvorenu zagradu -> izbacimo je sa steka 


test_ulaz = "(5+3) * ( 3 + 6 )" # primer dobrih zagrada
print(da_li_su_dobre_zagrade(test_ulaz))
test_ulaz = "(5+3) * )( 3 + 6 )" # primer sa vise zatvorenih u nekom trenutku
print(da_li_su_dobre_zagrade(test_ulaz))
test_ulaz = "(5+3) * ( 3 + 6 )((((" # primer sa vise otvorenih
print(da_li_su_dobre_zagrade(test_ulaz))


test_ulaz = "(5+3) * ( 3 + 6 )" # primer dobrih zagrada
print(zagrade_sa_stekom(stek,test_ulaz))
test_ulaz = "(5+3) * )( 3 + 6 )" # primer sa vise zatvorenih u nekom trenutku
print(zagrade_sa_stekom(stek,test_ulaz))
test_ulaz = "(5+3) * ( 3 + 6 )((((" # primer sa vise otvorenih
print(zagrade_sa_stekom(stek,test_ulaz))

