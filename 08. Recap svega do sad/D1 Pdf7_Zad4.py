# Napisati rekurzivan program koji uklanja cifre iz broja

def ukloni_cifre_rekurzivno(broj, cifra):
    if broj == 0:
        return []
    if broj%10 != cifra:
        return ukloni_cifre_rekurzivno(broj//10, cifra) + [broj%10]
    return ukloni_cifre_rekurzivno(broj//10, cifra)

def ukloni_cifre_rekurzivno_listom(lista_brojeva, cifra):
    if lista_brojeva == []:
        return []
    if lista_brojeva[-1] != cifra:
        return ukloni_cifre_rekurzivno_listom(lista_brojeva[:-1:], cifra) + [lista_brojeva[-1]]
    return ukloni_cifre_rekurzivno_listom(lista_brojeva[:-1:], cifra)



# Main

n = int(input("Unesite broj: "))
lista_n = [int(cifra) for cifra in str(n)]
cifra = int(input("Unesite cifru za uklanjanje: "))

rezultat = int("".join(str(i) for i in ukloni_cifre_rekurzivno(n, cifra)))
rezultat_listom = int("".join(str(i) for i in ukloni_cifre_rekurzivno_listom(lista_n, cifra)))
print(f"Rezultat (rekurzivno, bez liste) uklanjanja cifara {cifra} iz broja {n} je: {rezultat}.")
print(f"Rezultat (rekurzivno, sa listom) uklanjanja cifara {cifra} iz broja {n} je: {rezultat_listom}.")