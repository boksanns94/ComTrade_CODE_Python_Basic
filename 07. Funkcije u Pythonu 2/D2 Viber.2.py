# Napisati funkciju iterativno/rekurzivno koja racuna proizvod cifara nekog broja

# Iterativno
def iterativno_proizvod_cifara(broj = 0):
    proizvod = 1
    lista_cifara = [int(x) for x in str(broj)]
    for cifra in lista_cifara:
        proizvod *= cifra
    return proizvod

# Rekurzivno
def rekurzivno_proizvod_cifara(broj = 0):
    if broj == 0:
        return 1
    return broj%10 * rekurzivno_proizvod_cifara(broj//10)



# Main

n = int(input("Unesite broj: "))
print(f"Iterativna funkcija - proizvod cifara = {iterativno_proizvod_cifara(broj = n)}.")
print(f"Rekurzivna funkcija - proizvod cifara = {rekurzivno_proizvod_cifara(broj = n)}.")