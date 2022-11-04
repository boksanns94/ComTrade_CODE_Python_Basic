# Napisati rekurzivni program koji racuna sumu
# svih elemenata na pozicijama deljivim sa 3

# *** ja sam ovo razumeo da sabira elemente sa pozicija 4, 7, 11 itd
# *** tj sa pozicija ciji je index deljiv sa 3 (npr. lista[3] + lista[6] + lista[9])

def suma_elemenata_pozicija_3(lista_brojeva:list) -> int:
    if (len(lista_brojeva)-1)/3 < 1:
        return 0
    return lista_brojeva[3] + suma_elemenata_pozicija_3(lista_brojeva[3::])

# Ideja funkcije koja sabira elemente sa pozicija koji su deljivi sa brojem n
# Ako je n == 0 ne sabira nista u listi i vraca 0 (jer ni jedna pozicija nije deljiva sa 0)
# Ako je n == 1 sabira sve elemente liste, jer su sve pozicije deljive sa 1
# ------------------------------------------------------------
# def suma_elemenata_pozicija_n(lista_brojeva:list, n:int) -> int:
#     if n == 0:
#         return 0
#     if n == 1:
#         return sum(lista_brojeva)
#     if (len(lista_brojeva)-1)/n < 1:
#         return 0
#     return lista_brojeva[n] + suma_elemenata_pozicija_n(lista_brojeva[n::], n)



# Main

n = int(input("Unesite broj: "))
lista_n = [int(znak) for znak in str(n)]
rezultat = suma_elemenata_pozicija_3(lista_n)
print(f"Rezultat sume nad brojem {n} je: {rezultat}.")