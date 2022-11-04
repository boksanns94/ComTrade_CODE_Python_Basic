# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:13:21 2021

@author: Boksan
"""
 # osnovno
print("zdravo svete, sta ima")
print('zdravo svete ponovo')

# proba escape karaktera
print("Milos Boksan \n asdasd")
print("ja sam \"programer\"")
print('i ja sam "programer"')
print("A ja sam rekao \"Hej, dodji ovamo!\"")

# menjanje krajnjeg dodavanja novog reda u print komandi
print("neki teskt a posle toga ide:", end = 'tekst')
print("neki teskt a posle toga ide:", end = "tekst")

#primer printa kada se ubacuje vise argumenata, onda print dodaje razmak
print("milos","boksan","radnik","ucenik")
#menjanje karaktera koji odvaja ove ispise sa argumentom sep
print("milos","boksan","radnik","ucenik", sep=", ")

#primer konkatenacije teksta u printu
# "sabiranje" teksta
print("Milos" + "Boksan")

#ispis broja
print(123)
#ispis teksta i broja
print("tekst", 123)
#ovo ne moze
# print("tekst" + 123) <- izbaci gresku

#stampanje rezultata racunice u printu
print(1+2+3+4+5)

#vezba 1
#ispisati 2+2=4; ponovo ali bez koriscenja tastera 4 na tastaturi
print("2+2=4")
print("2+2=", 2+2)
print("2+2=", 2+2, sep="")
















