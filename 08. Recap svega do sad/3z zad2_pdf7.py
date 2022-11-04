# 1234 
# 4 -> > 1 + rek(123) = 1 +3 = 4 
# rek(123) -> 1 + rek(12) = 1+2=3 
# rek(12) = 1 + rek(1) = 1+1 =2 
# rek(1) = 1 + rek(0) = 1 
# rek(0) = 0
# napisati rekurziju koja broji koliko cifara ima neki broj 
def prebroj_cifre_rekurzivno(broj):
    print(broj)
    if broj == 0:
        return 0
    return 1 + prebroj_cifre_rekurzivno(broj//10)
print(prebroj_cifre_rekurzivno(12345))

def brojac_parnih_cifara(broj):
    if broj == 0:
        return 0
    poslednja_cifra = broj % 10
    print("Poslednja cifra trenutnog broja je ",poslednja_cifra,"a broj je ",broj)
    if poslednja_cifra % 2 == 0:
        return 1 + brojac_parnih_cifara(broj//10)
    else:
        return 0 + brojac_parnih_cifara(broj//10)

def zbir_parnih_cifara(broj):
    if broj == 0:
        return 0
    poslednja_cifra = broj % 10
    print("Poslednja cifra trenutnog broja je ",poslednja_cifra,"a broj je ",broj)
    if poslednja_cifra % 2 == 0:
        return poslednja_cifra + zbir_parnih_cifara(broj//10)
    else:
        return 0 + zbir_parnih_cifara(broj//10)


# 5724 ->   4 ili rek(572) = 4 ili 7 -> 7 veca je rekurzija ostatka -> rekurzija_ostatka
# rek(572) -> 2 ili rek(57) = 2 ili 7 = 7  veca je rekurzija ostatka -> rekurzija_ostatka
# rek(57) -> 7 ili rek(5) -> 7 ili 5 -> 7 poslednja cifra je veca od rekurzije ostatka -> poslednja_Cifra
# rek(5) -> 5 ili rek(0) -> 5 ili 0 -> 5 poslednja cifra je veca od rekurzije ostatka -> poslednja_Cifra
# rek(0) -> 0
def najveca_cifra_rekurzivno(broj):
    if broj == 0:
        return 0 
    poslednja_cifra = broj % 10
    maksimum_ostatka = najveca_cifra_rekurzivno(broj//10)
    if poslednja_cifra > maksimum_ostatka:
        return poslednja_cifra
    else:
        return maksimum_ostatka

print(najveca_cifra_rekurzivno(5724))
    