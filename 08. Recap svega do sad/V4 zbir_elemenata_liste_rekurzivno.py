# izracunati sumu svih elemenata liste uz rekurziju
# [1,2,3,4,5] = 15 suma
# suma = lista.pop() + rekurzija_suma(lista.pop())

def rekurzija_suma(lista_brojeva):
    if len(lista_brojeva) == 1:
        return lista_brojeva.pop()
    return lista_brojeva.pop() + rekurzija_suma(lista_brojeva)



# Main

n = int(input("Unesite duzinu liste: "))
lista_brojeva = [int(input("Unesite element: ")) for i in range(n)]
print(f"Suma elemenata liste {lista_brojeva} je {rekurzija_suma(lista_brojeva)}.")