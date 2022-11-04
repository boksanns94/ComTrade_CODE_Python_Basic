# Napisati rekurzivnu funkciju koja
# obrce cifre datog celog broja.
# Zadatak se moze resiti koriscenjem listi.

def obrni_listu_rekurzivno(lista_brojeva):
    if len(lista_brojeva) == 0:
        return []
    return [lista_brojeva[-1]] + obrni_listu_rekurzivno(lista_brojeva[:-1:])



# Main

n = int(input("Unesite broj: "))
lista_n = [int(cifra) for cifra in str(n)] # pretvaram broj n u listu cifara
obrnut_n = int("".join(str(i) for i in obrni_listu_rekurzivno(lista_n))) # vracam obrnutu listu u int
print(f"Redovan broj: {n}. Obrnut broj: {obrnut_n}")