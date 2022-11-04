# Napisati rekurzivnu funkciju palindrom(niz)
# koja ispituje da li su elementi nekog
# niza brojeva poređani palindromski
# (isto napred i od pozadi).

# anavolimilovana
# niz0 + rek ostatak + niz-1
# len(1) or len(0) return

def palindrom_rekurzivno(lista):
    if len(lista) == 0:
        return True
    if lista[0] == lista[-1]:
        return palindrom_rekurzivno(lista[1:-1:1])



# Main

rec = input("Unesite rec za proveru palindroma: ")
if palindrom_rekurzivno(rec):
    print(f"Rec {rec} jeste palindrom.")
else:
    print(f"Rec {rec} nije palindrom.")