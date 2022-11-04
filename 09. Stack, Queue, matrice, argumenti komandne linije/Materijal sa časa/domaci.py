
# rekurzijom treba pronaci najmanji element u listi
def minimum_rekurzija(brojevi):
    if len(brojevi) == 1: # ako  smo ostlai na jednom elementu 
        return brojevi[0] # taj element je minimum liste
    minimum_ostatka = minimum_rekurzija(brojevi[1:])
    prvi_element = brojevi[0]
    if prvi_element < minimum_ostatka:
        return prvi_element
    else:
        return minimum_ostatka
    # return prvi_element if prvi_element < minimum_ostatka else minimum_ostatka
    
    #a = vrednodst_ako_je_uslov_tacan USLOV else vrednodst_ako_je_uslov_nije_tacan

brojevi=[34,12,234,23,34]
print(minimum_rekurzija(brojevi))
# 0  1  2   3  4   5 6 7 8 9
# 34 12 234 23 34 10 1 2 3 4
def suma_pozicija_koje_su_deljive_sa_3(brojevi):
    if len(brojevi) == 0:
        return 0
    return brojevi[0] + suma_pozicija_koje_su_deljive_sa_3(brojevi[3:])
x = list(range(1,10))
# 1 2 3 4 5 6 7 8 9
print(suma_pozicija_koje_su_deljive_sa_3(x))

def suma_drugi(brojevi,pozicija=0):
    if pozicija == len(brojevi):
        return 0
    if pozicija % 3 ==0:
        return brojevi[pozicija] + suma_drugi(brojevi,pozicija+1)
    else:
        return suma_drugi(brojevi,pozicija+1)
print(suma_drugi(x))
def suma_treci(brojevi,pozicija=0):
    if pozicija >= len(brojevi):
        return 0
    return brojevi[pozicija] + suma_treci(brojevi,pozicija+3)
print(x)
x.append(10)
print(x)
print(suma_treci(x))

def ubaci_nule(broj):
    if broj == 0:
        return []
    poslednja_cifra = broj%10
    if poslednja_cifra % 2 != 0:
        #return [poslednja_cifra,0] + ubaci_nule(broj//10)
        return ubaci_nule(broj//10) + [poslednja_cifra,0]
    else:
        #return [poslednja_cifra] + ubaci_nule(broj//10)
        return ubaci_nule(broj//10) + [poslednja_cifra]

print(ubaci_nule(1234))