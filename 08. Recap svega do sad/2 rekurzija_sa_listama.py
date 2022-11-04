
# uz pomoc rekurzije izracunam zbir svih elemenata liste.
#       0 1 2 3 4 5 6
# suma([1,2,3,4,1,2,3])
# 1 + suma[2,3,4,1,2,3] = 1+15 =16
# suma([2,3,4,1,2,3]) = 2 + suma([3,4,1,2,3]) = 2 + 13 = 15
#  suma[3,4,1,2,3] = 3 +  suma([4,1,2,3]) = 3 + 10 = 13 
# suma[4,1,2,3] = 4 + suma([1,2,3]) = 4+6=10 
# suma[1,2,3] = 1 + suma([2,3]) = 1+5=6
# suma[2,3] = 2 + suma([3]) = 2+3=5
# suma[3] = 3 + suma [] = 3+0 = 3 
# suma [] = 0 kada stignemo do kraja liste tj ako je len(liste) == 0
# onda vracamo 0 kao rezultat
brojevi = [1,2,3,4,1,2,3]
# print(brojevi[0])
# print(brojevi[1:])
def rekurzija_suma(lista_brojeva):
    print(lista_brojeva)
    if len(lista_brojeva) == 0:
        return 0
    print("Rezultat ce biti",lista_brojeva[0],"+ poziv za",lista_brojeva[1:])
    return lista_brojeva[0] + rekurzija_suma(lista_brojeva[1:])
print(rekurzija_suma(brojevi))
def rekurzija_suma_sa_podrazumevanim_argumentom(brojevi,pozicija=0):
    if pozicija == len(brojevi):
        return 0
    return brojevi[pozicija] + rekurzija_suma_sa_podrazumevanim_argumentom(brojevi,pozicija+1)
    # 5 + rekurzija(brojevi,pozicija+1) = 5 + 13 = 18
    # pozicija:1 
    # 6 + rekurzija(brojevi,2) = 6+7 =13 
    # pozicija:2
    # 7 + rekurzija(brojevi,3) = 7 + 0 = 7
    # rekurzija(brojevi,3) -> 0
#          0 1 2
brojevi = [5,6,7]
print(rekurzija_suma_sa_podrazumevanim_argumentom(brojevi))
print(rekurzija_suma_sa_podrazumevanim_argumentom([]))
#print(1000 + None)
    
    