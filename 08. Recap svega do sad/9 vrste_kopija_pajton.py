
l1 = [1,2,3,[3,4]]
l2 = l1 
print(l1,l2)
l2[0] = 123
l1[1] = 100
print(l1,l2)

print(id(l1),id(l2))
print(id(l1[0]),id(l2[0]))

def dodaj_el(lista):
    lista.append(10)

test = []

dodaj_el(test)
print(test)
dodaj_el(test)
print(test)
dodaj_el(test)
print(test)
dodaj_el(test)
print(test)
def promeni(x):
    x+=5

x=10
promeni(x)
print(x)
# shallow copy
l1 = [1,2,3,[3,4]]
l2 = l1.copy() # pozovemo metodu copy nad nekom listom 

print(l1,l2)
print(id(l1),id(l2))
print(id(l1[0]),id(l1[1]),id(l1[2]),id(l1[3]))
print(id(l2[0]),id(l2[1]),id(l2[2]),id(l2[3]))

l2[0] = 5 
print(l1,l2)
print(id(l1[0]),id(l2[0]))
print(l2[3]) 
print(l2[3][1])

l2[3][1] = 100
print(l1,l2)

from copy import deepcopy 
# from naziv_modula import neka_funkcija,klasa,metoda....
# -> pozivate funkciju sa samo naziv_funkcije
import math # import naziv_modula
print(math.sqrt(16)) # da bih iskoristio nesto iz modula moram da kazem naziv_modula.naziv_fje
print(math.pi)
# deepcopy prica
l1 = [1,2,3,[3,4]]
l2 = deepcopy(l1)
print(l1,l2)
l2[3][0]=123
print(l1,l2)


a=1000
b=1000
print(id(a),id(b))
brojevi=[1000,123]
print(id(brojevi[0]))