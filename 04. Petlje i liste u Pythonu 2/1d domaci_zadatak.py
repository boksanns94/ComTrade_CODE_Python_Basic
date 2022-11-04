#          0 1 2 3 4 5  6 
brojevi = [3,4,6,1,2,3,45]

# treba da se ispisu svi elementi od predposlednjeg do drugog elementa u listi ( pozicija 1 ) 
print(brojevi[-2:0:-2])

# ispis preko pozicija 
# ispis prolaskom kroz listu sa privremenom promenljivom
n = len(brojevi) # n - predstavlja duzinu liste, odnosno broj elemenata u listi
# sama lista u sebi ima elemente na pozicijama od 0 do duzina - 1 , tj od 0 do n-1 
for i in range(n-2,0,-2):
    print(brojevi[i],end=" ")
print()
for broj in brojevi[-2:0:-2]:
    print(broj,end=" ")

    
