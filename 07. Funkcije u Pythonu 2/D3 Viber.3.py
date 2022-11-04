# Napisati rekurzivno funkciju koja racuna najvecu cifru u broju
# Ako nije naveden broj, podrazumevano uzima vrednost 0

def najveca_cifra(broj = 0, max_cifra = 0):
    if broj == 0:
        return(max_cifra)
    if broj % 10 > max_cifra:
        return najveca_cifra(broj//10, max_cifra = broj % 10)
    return najveca_cifra(broj//10, max_cifra)



# Main

n = int(input("Unesite broj: "))
print(f"Najveca cifra broja {n} je {najveca_cifra(n)}.")