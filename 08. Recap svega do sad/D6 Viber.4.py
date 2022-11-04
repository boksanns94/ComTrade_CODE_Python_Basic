# Napisati rekurzivnu funkciju koja proverava da li se neka uneta cifra nalazi u unetom broju

def pojavljivanje_cifre(broj, cifra):
    if len(str(broj)) == 1 and broj == 0:
        return False
    if broj%10 == cifra:
        return True
    return pojavljivanje_cifre(broj//10, cifra)



# Main

n = int(input("Unesite broj: "))
cifra = int(input("Unesite cifru koju trazimo: "))
if pojavljivanje_cifre(n, cifra) == True:
    print(f"U broju {n} postoji cifra {cifra}.")
else:
    print(f"U broju {n} ne postoji cifra {cifra}.")