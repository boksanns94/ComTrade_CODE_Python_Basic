# pdf zad2 

# Napisati program
# koji učitava pozitivan ceo broj n, a potom i n realnih brojeva.
# Program ispisuje koliko puta je prilikom unosa došlo do promene znaka. Do
# promene znaka dolazi kada se nakon pozitivnog broja unese negativan broj ili
# kada se nakon negativnog broja unese pozitivan broj. U slučaju neispravnog
# unosa, ispisati odgovarajuću poruku o grešci.

n = int(input("Unesite duzinu liste:"))

brojevi = []
for i in range(n):
    unos = float(input("Unesite neki realan broj:"))
    brojevi.append(unos)
    
print(brojevi)
brojac = 0 
# 0 1 2 3 4 
# treba da proverimo da li je doslo do promene znaka 
# Moramo da poredimo uzastopne elemente u listi
#  i    i+1
# [0]  [1] 
# [1]  [2] 
# [2]  [3]
# [3]  [4] 

for i in range(n-1): # prolazimo kroz listu koriscenjem pozicija 
    # if brojevi[i] >= 0 and brojevi[i+1] < 0:
        # brojac = brojac + 1 
    # if brojevi[i] < 0 and brojevi[i+1] >= 0:
        # brojac = brojac + 1
    # if (brojevi[i] >= 0 and brojevi[i+1] < 0) or (brojevi[i] < 0 and brojevi[i+1] >=0):
        # brojac = brojac + 1 
    if brojevi[i] * brojevi[i+1] <= 0:
        brojac = brojac + 1 
    
print(brojac)



