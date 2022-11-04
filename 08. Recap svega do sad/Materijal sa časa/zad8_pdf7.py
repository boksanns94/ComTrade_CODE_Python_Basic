# 012345678901234
# anavolimilovana
# navolimilovan
# avolimilova
# volimilov
# olimilo
# limil
# imi
# m
# "" -> True

# abca
# a!=a -> 
# bc 
# b!=c -> False
lista = "anavolimilovana"
while len(lista) > 0:

    print(lista[1:-1])
    lista=lista[1:-1]
# -> navolimilovan
def palindrom(lista):
    if len(lista) == 0:
        return True
    if lista[0] != lista[-1]: # ako je prvi element (poz 0 ) razlicit makar jednom
        # od poslednje pozicije [-1] onda on nije palindrom
        return False
    return palindrom(lista[1:-1])
print(palindrom("anavolimilovana"))
print(palindrom("oko"))
print(palindrom("kapak"))
print(palindrom("kuk"))
print(palindrom("qwe"))
# 0  1  2  3  4 
# 1  2  3  2  1
# duzina liste je 5
#  i       n-i-1
# [0] <-> [4]
# [1] <-> [3]
# [2] <-> [2]
# [3] <-> [1]
# [4] <-> [0]
def bez_rek_palindrom(lista):
    pretpostvka = True
    for i in range(len(lista)):
        if lista[i] != lista[-i-1]:
            pretpostvka = False
            break
    return pretpostvka
def palindrom_jos_lakse(lista):
    return lista[::-1] == lista

print(palindrom_jos_lakse("anavolimilovana"))

    

