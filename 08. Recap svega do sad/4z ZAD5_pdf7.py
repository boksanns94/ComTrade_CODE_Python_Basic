
# # Napisati
# rekurzivnu funkciju napravi_niz(broj) koja kreira niz cifara datog celog
# broja. Napisati rekurzivnu funkciju ispisi_niz(niz, index) koja ispisuje elemente niza
# dužine n. Testirati obe funkcije pozivom iz glavnog programa.
# 552 -> [2] + rek(55) = [2] + [5,5] = [2,5,5]
# rek(55) -> [5] + rek(5) =[5] + [5] = [5,5]
# rek(5) -> [5] + rek(0) =[5] + [] = [5]
# rek(0) -> []
l1 = [1,2,3]
l2 = [4,5,6]
print(l1+l2,l1,l2)
l1.extend(l2)
print(l1)
l3 = l1 + l2
print(l3)

def napravi_niz(broj):
    if broj == 0:
        return []
    poslednja_cifra = broj%10
    return [poslednja_cifra] + napravi_niz(broj//10)
print(napravi_niz(1234))
def napravi_niz_unapred(broj):
    if broj == 0:
        return []
    poslednja_cifra = broj % 10 
    ostatak = napravi_niz_unapred(broj//10)
    print(ostatak,broj)
    return ostatak + [poslednja_cifra]
print(napravi_niz_unapred(1234))

# print([123] + [1,2,3])