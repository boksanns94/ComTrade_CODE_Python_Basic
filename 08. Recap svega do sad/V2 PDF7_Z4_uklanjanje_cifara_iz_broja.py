# Napisati program koji uklanja cifre iz broja

# Uklanjanje cifara iz liste

def ukloni_cifre(broj, cifra):
    lista_brojeva = [int(cifra) for cifra in str(broj)] # Pretvaranje int u list
    broj_ponavljanja = lista_brojeva.count(cifra)
    for j in range(broj_ponavljanja):
        lista_brojeva.remove(cifra)
    return int("".join(str(i) for i in lista_brojeva)) # Pretvaranje list u int

    

# Main

n = int(input("Unesite broj: "))
cifra = int(input("Unesite cifru za uklanjanje: "))
print(f"Rezultat uklanjanja cifara {cifra} iz broja {n} je: {ukloni_cifre(n, cifra)}.")