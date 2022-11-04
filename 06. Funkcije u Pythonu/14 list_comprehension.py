# list comprehension

brojevi = [3,4,1,2,3,4,5,6,7]
# napravimo listu samo parnih brojeva 
parni = []
for broj in brojevi:
    if broj % 2 == 0:
        parni.append(broj)
        
print(parni)

#nova_lista = [sta_ubacujem prolazak_kroz_listu uslov]
p = [broj for broj in brojevi if broj % 2 == 0]
print(p)
# unos liste duzine n
n=5

def prost(broj): 
    for i in range(2,broj//2+1):
        if broj % i == 0:
            return False
    
    return True
unos = [int(input("Unesite broj:")) for i in range(n)]
print(unos)
lista_prostih = [i for i in range(2,100) if prost(i)]
print(lista_prostih)
broj = 1234
broj = str(1234)

cifre = [int(c) for c in broj]
print(cifre)
print(cifre)