# Napisati rekurzivan program koji broji parne cifre u broju

def brojac_parnih_cifara_rekurzivno(broj):
    if broj == 0:
        return 0
    if (broj%10)%2 == 0:
        return 1 + brojac_parnih_cifara_rekurzivno(broj//10)
    else:
        return 0 + brojac_parnih_cifara_rekurzivno(broj//10)



# Main

n = int(input("Unesite broj: "))
print(f"Broj parnih cifara u broju {n} je {brojac_parnih_cifara_rekurzivno(n)}.")