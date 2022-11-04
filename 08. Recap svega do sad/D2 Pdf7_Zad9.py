# Napisati rekurzivnu funkciju dodaj_nulu(x)
# koja posle svake neparne cifre datog broja dodaje 0.

def dodaj_nulu_rekurzivno(broj):
    if len(broj) == 0:
        return []
    if broj[0] % 2 != 0:
        osnova = [broj[0]] + [0]
        osnova.extend(dodaj_nulu_rekurzivno(broj[1::]))
        return osnova
    osnova = [broj[0]]
    osnova.extend(dodaj_nulu_rekurzivno(broj[1::]))
    return osnova



# Main

n = int(input("Unesite broj: "))
lista_n = [int(cifra) for cifra in str(n)]
rezultat = int("".join(str(i) for i in dodaj_nulu_rekurzivno(lista_n)))
print(f"Rezultat dodavanja nula u broj {n} je {rezultat}.")