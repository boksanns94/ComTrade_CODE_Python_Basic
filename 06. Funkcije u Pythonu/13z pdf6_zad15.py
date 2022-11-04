# pdf6_zad15
# napisati funkciju koja kao argument prima neki broj, i kao rezultat vraca listu njegovih
# cifara

def vrati_listu_cifara(broj):
    # broj = abs(broj)
    if broj < 0:
        broj = -broj 
        
    lista_cifara = []
    while broj > 0:
        poslednja_cifra = broj % 10
        broj //= 10
        
        lista_cifara.append(poslednja_cifra)
    
    return lista_cifara[::-1]

    
# cifre = vrati_listu_cifara(1234)
# print(cifre)
prvi = int(input("Unesite broj:"))
drugi = int(input("Unesite broj:"))
lista_cifara_prvi = vrati_listu_cifara(prvi)
lista_cifara_drugi = vrati_listu_cifara(drugi)
if sorted(lista_cifara_prvi) == sorted(lista_cifara_drugi):
    print("da")
else:
    print("ne")
    
def vrati_listu_broja_ponavljanja_svake_cifre(broj):
#                  0 1 2 3 4 5 6 7 8 9
    ponavljanja = [0,0,0,0,0,0,0,0,0,0]
    broj = abs(broj)
    while broj > 0:
        poslednja_cifra = broj % 10
        broj //=10 
        
        ponavljanja[poslednja_cifra] += 1 
        #print(ponavljanja)
    return ponavljanja
vrati_listu_broja_ponavljanja_svake_cifre(31231231)
if vrati_listu_broja_ponavljanja_svake_cifre(prvi) == vrati_listu_broja_ponavljanja_svake_cifre(drugi):
    print("da")
else:
    print("ne")
        
        
    
    