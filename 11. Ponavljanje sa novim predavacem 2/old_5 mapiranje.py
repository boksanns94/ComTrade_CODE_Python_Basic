
brojevi = [1,2,4,5,-10]
def dodaj_10(x):
    return x+10
promeni = lambda x: x**2 # naziv = lambda arg1,arg2: rezultat
print(promeni(2))
print(list(map(dodaj_10,brojevi)))

print(list(map(lambda x:x+10,brojevi)))

prva = [1,2,3]
druga = [4,5,6]
def saberi(x,y):
    return x+y
print(list(map(saberi,prva,druga)))
print(type(saberi))

print(list(filter(lambda x: x%2 == 0,brojevi)))
def prost(broj):
    if broj == 1:
        return False
    for i in range(2,broj//+1):
        if broj % i == 0:
            return False
    return True

print(list(filter(prost,brojevi)))
print(list(filter(dodaj_10,brojevi)))
