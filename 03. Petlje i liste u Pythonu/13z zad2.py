#zad 2 sa pdf-a
# dodatak naterati korisnika da ispravno unese broj ponavljanja
brojevi = [3,4,5,1,1,1]
brojevi = brojevi[::-1]
for broj in brojevi:
    print(broj,end=" ")

for i in range(len(brojevi)-1,-1,-1):
    print(brojevi[i],end=" ")
n= int(input("Unesite n:"))

while n<= 0:
    n = int(input("Unesite POZITIVAN BROJ!\n"))

for i in range(n): # i uzima vrednosti od 0 do n-1 -> n ponavljanja
    print("Mi volimo da programiramo")
    
    