# kljucni argumenti (keyword arguments)

def podeli(a,b):
    return a/b if b != 0 else None
    
# a = 6
# if a % 2 == 0:
    # b = 10 
# else:
    # b = 20
# b = 10 if a % 2 == 0 else 20

# print(b)

c=10
d=5
print(podeli(a=c,b=d))
print(podeli(b=d,a=c))
print(podeli(c,b=d))
#print(podeli(d,a=c))

def podrazumevani_zbir(prvi,drugi=10):
    return prvi + drugi

print(podrazumevani_zbir(5,123))
print(podrazumevani_zbir(5))
def suma_nepoznata(*brojevi):
    print(brojevi)
    zbir = 0
    for broj in brojevi:
        print(broj,end=" " )
        zbir += broj
    return zbir
print(suma_nepoznata(1,2,3,1,2))
print(suma_nepoznata(1,2,3,1,2,123,1,2,3,43,5))

brojevi = [1,2,3,4,1,2,3]
print(brojevi)
print(*brojevi)
#brojevi = *brojevi

def zbirzbir(a,b,c=2):
    return a+b+c

print(zbirzbir(1,b=2))
print(zbirzbir(1,2,3))
print(zbirzbir(2,3,c=5))
#print(zbirzbir(2,a=1))
print(zbirzbir(1,b=2))
print(zbirzbir(1,c=5,b=3))