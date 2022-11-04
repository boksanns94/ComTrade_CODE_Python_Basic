# Napisati rekurzivnu funkciju koja proverava da li je uneti broj prost

def da_li_je_prost(broj, delilac = 2):
    if broj/delilac < 2:
        return True
    if broj%delilac == 0:
        return False
    return da_li_je_prost(broj,delilac+1)
    



# Main

n = int(input("Unesite broj: "))
rezultat = da_li_je_prost(n)
if rezultat == True:
    print(f"Broj {n} jeste prost broj.")
else:
    print(f"Broj {n} nije prost broj.")