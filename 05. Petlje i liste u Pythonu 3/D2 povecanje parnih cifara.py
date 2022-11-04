# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 20:57:24 2021

@author: Boksan
"""

broj = int(input("Unesite broj: "))
while int(broj) <= 0:
    broj = int(input("Greska. Ponovo: "))

temp_broj = broj # pravim kopiju broja da imam original za ispis na kraju
pozicija_cifre = 0 # pracenje da li sam na jedinicama, deseticama, stotinama...
rezultat = 0

while temp_broj != 0:
    cifra = temp_broj % 10 # izdvajam cifru najmanje tezine
    if cifra % 2 == 0: # pitam da li je parna
        rezultat += (cifra+1)*(10**pozicija_cifre)  # dodajem cifru uvecanu za 1, puta eksponent 10ke 
                                                    # u zavisnosti od pozicije cifre u originalnom broju
                                                    # ako je na poziciji jedinice onda je 10**0
                                                    # ako je na poziciji desetice onda je 10**1...
    else:
        rezultat += cifra*(10**pozicija_cifre) # ako je neparna opet je dodajem, ali se ne uvecava za 1
    pozicija_cifre += 1 # pratimo poziciju cifre
    temp_broj //= 10 # "pop-ujem" odradjenu cifru

print(f"Rezultat izmene broja {broj} je {rezultat}.")

# =============================================================================
# pitanje za cas:
# pokusao sam da uradim ovo i sa negativnim brojevima
# i uspeo sam tako sto na pocetku pretvorim broj u
# pozitivan i zapamtim da je bio negativan i na kraju
# prosto opet promenim znak.
# Ali kad sam pokusao da uradim sledecu stvar
# -124 % 10
# dobijem rezultat
# 6
# a ocekivao sam
# 4
# zasto?
# =============================================================================
