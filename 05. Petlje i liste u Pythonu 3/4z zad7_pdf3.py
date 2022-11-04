# Pravi delioci celog broja su svi delioci osim jedinice i samog tog broja. Napisati
# program koji za uneti pozitivan ceo broj n ispisuje sve njegove prave delioce. U
# slučaju neispravnog unosa ispisati odgovarajuću poruku o grešci.

n = int(input("Unesite ceo broj:"))

if n < 0:
    print("Los unos.")
    exit()


# 20 sa kojim sve brojevima je deljiv ?
# (1) 2 4 5 10  (20)

# for i in range(2,n//2+1): # i uzima sve vrednosti od 2 do n-1 
   # print(i,end=" ")
    # if n % i == 0:
        # print(i,end=" ")
        
# Za neki broj, proveriti da li je prost. 
# Broj je prost, ako je deljiv samo sa sobom i sa jedinicom.
brojac = 0
for i in range(2,n//2 + 1 ):
    if n % i == 0:
        brojac = brojac + 1 
        break

if brojac == 0:
    print(n,"je prost")
else:
    print(n,"nije prost")
    
pretpostavka_da_je_prost = True # pretpostavicemo da jeste prost
for i in range(2,n//2+1): # trazimo kontra primer
# ako je deljiv sa makar jos jednim brojem izmedju 2 i broj pola 
    if n % i == 0:
        pretpostavka_da_je_prost = False # onda nije prost
        # menjamo flag na false
        break # iskacemo iz petlje 
if pretpostavka_da_je_prost == True:
    print(n,"je prost")
else:
    print(n,"nije prost")
    
print(6/2)
print(7//2)

print(abs(-123)) # abs(neki_broj) -> vraca apsolutnu vrednost broja 

    
        
        