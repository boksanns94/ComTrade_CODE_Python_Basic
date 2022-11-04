# pdf 3 zadatak 5

# korisnik unosi n, ako je n negativno ispisati odgovarajucu gresku.
# u slucaju da je n validno ispisati faktorijel od n
# 5! = 1*2*3*4*5 ( proizvod svih brojeva od 1 do tog samog broja )
n = int(input("Unesite neki broj, za koji trazimo faktorijal:"))

if n < 0:
    print("Los unos,unos mora biti pozitivan broj!")
    exit()
    
# trazimo proizvod -> treba nam promenljiva za proizvod koja je na pocetku jednaka 1 
proizvod = 1 
# n= 6 -> 1 2 3 4 5 6
for i in range(1,n+1): # n+1 jer y nije ukljuceno u opseg 
    
    proizvod = proizvod * i # svaki put stari proizvod mnozimo sa i, zasto sa i -> i uzima sve vrednosti od 1 do n 
    print(f"Trenutno i je {i}, a proizvod je {proizvod}")
print(f"{n}! = {proizvod}")