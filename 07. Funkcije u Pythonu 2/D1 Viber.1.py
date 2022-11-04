# Napisati funkciju koja kao argument prima neki broj i racuna
# sumu svih njegovih delilaca (osim tog broja). 
# Uraditi rekurzivno.
# Ako nije naveden broj, podrazumevano uzima vrednost 0
# Sve funkcije pozivati uz pomoc kljucnih argumenata i pozicionih

def sabiranje_delilaca_broja(n = 1, delilac = 1):
    if delilac > n//2:
        return 0
    if n % delilac == 0:
        return delilac + sabiranje_delilaca_broja(n, delilac + 1)
    else:
        return 0 + sabiranje_delilaca_broja(n, delilac + 1)



# Koristeci proslu funkciju, napisati funkciju
# koja proverava a li je net broj savrsen broj. 
# Broj je savrsen, ako je jednak sumi svojih delilaca.

def da_li_je_savrsen_broj(broj):
    if broj == sabiranje_delilaca_broja(broj):
        return True



# Main

n = int(input("Unesite broj n: "))
print(f"Suma delilaca broja {n} je {sabiranje_delilaca_broja(n)}.")
if da_li_je_savrsen_broj(n):
    print(f"Broj {n} jeste savrsen broj.", end = "")
else:
    print(f"Broj {n} nije savrsen broj.", end = "")