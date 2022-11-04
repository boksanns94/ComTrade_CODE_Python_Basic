# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 17:38:43 2021

@author: Boksan
"""

moja_promenljiva = input("Unesite moju promenljivu: ")
print(moja_promenljiva)
#print(MOJA_PROMENLJIVA)
#u liniji 10 izbacuje gresku

prvi_broj = input("Unesi 1. br:")
drugi_broj = input("Unesi 2. br:")
print("Prvi broj je: ", prvi_broj)
print("Drugi broj je: ", drugi_broj)

temp = prvi_broj
prvi_broj = drugi_broj
drugi_broj = temp
print("posle prve zamene: ")
print("Prvi broj je: ", prvi_broj)
print("Drugi broj je: ", drugi_broj)

prvi_broj, drugi_broj = drugi_broj, prvi_broj
print("posle druge zamene: ")
print("Prvi broj je: ", prvi_broj)
print("Drugi broj je: ", drugi_broj)



#primeri lose stampe
a = 2
b = 6.9
c = 420.420
# istampati a + b + c = rezultat
print(a, "+", b, "+", c, "=", a+b+c)
#printom je tesko stampati

#funkcija format je bolja
print("{} + {} + {} = {}:".format(a,b,c,a+b+c))
print("{3} + {2} + {1} = {0}:".format(a,b,c,a+b+c))
print("{:<10.2f} tekst".format(c))

#f stringovi
print(f"{a} + {b} + {c:<10.2f} = {a+b+c}")



#castovanje
unos = input("broj:")

ceo_broj = int(unos)
print(ceo_broj)
decimalan_broj = float(unos)
print(decimalan_broj)
tekst = str(unos)
print(tekst)
logicka_bool = bool(unos)
print(logicka_bool)




#operatori poredjenja
# <  <=  >  >=
print("5>3",5>3)
print("7<1",7>1)
print("10>=10",10>=10)
print("2<=3",2<=3)

# == jednako
# != nejednako
print("5==5",5==5)
print("10!=10.0",10!=10.0)
print("\"asd\"!=55","asd"!=55)

#castovanje u BOOLEAN
print(bool(55))
print(bool(-555))
print(bool(-123.23))
print(bool("asd"))

print(bool(0))
print(bool(""))
print(bool(None))