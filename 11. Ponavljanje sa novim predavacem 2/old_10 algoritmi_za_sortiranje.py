brojevi = [5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3]
# 1. 
# 0 i 1 -> 5>1 -> 1 5 4 2 3
# 1 i 2 -> 5>4 -> 1 4 5 2 3
# 2 i 3 -> 5>2 -> 1 4 2 5 3
# 3 i 4 -> 5>3 -> 1 4 2 3 5
# Bubble sort
# 
# kraj prvog prolaska,poslednja cifra je najveca
# 1 4 2 3 5
# 0 i 1 -> 1 nije vece od 4 -> ne diramo
# 1 i 2 -> 4 > 2 -> 1 2 4 3 5
# 2 i 3 -> 4>3 -> 1 2 3 4 5
n = len(brojevi)
print(brojevi)
import time
now = time.time()
print(now)
for i in range(n-1): # zasto n-1 -> u svakom prolasku fiksiramo na kraj jednu poziciju najveceg
    # samim tim kada nam ostane 2 elementa, kada se oni zamene lista je sortirana
    for j in range(n-1-i):
        if brojevi[j] > brojevi[j+1]:
            brojevi[j],brojevi[j+1] = brojevi[j+1],brojevi[j]
        print(brojevi)
after = time.time()
print(after - now)

# Selection sort 
# 
# 
# brojevi = [5,1,4,2,3]
# 1. promenljiva i fiksira poziciju 0
# i svaki put poredi poziciju 0 sa svim ostalim pozicijama desno od nje
# 5>1 -> 1 5 4 2 3
# 1>4 -> ne menjamo
# 1>2,1>3 -> ne menjamo nista
# posle prvog kruga lista : 1 5 4 2 3
# 2. prolazak
# pozicija 1 je fiksirana
# 5>4 -> 1 4 5 2 3
# 4>2 -> 1 2 5 4 3
# 2>3 -> ne menja se
# na kraju drugog kruga fiksirana je druga pozicija
# 1 2 5 4 3
# fiksiramo poziciju 2
# 5>4 -> 1 2 4 5 3
# 4>3 -> 1 2 3 5 4
# na kraju ovog kruga ima mo 1 2 3 5 4
# fiksiramo poziciju 3 
# 5>4 -> 1 2 3 4 
brojevi = [5,1,4,2,3]
print(brojevi)
n=len(brojevi)
for i in range(n-1):
    for j in range(i+1,n):
        if brojevi[i] > brojevi[j]:
            brojevi[i],brojevi[j] = brojevi[j],brojevi[i]
            print(brojevi)
brojevi = [5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3,5,1,4,2,3]
now = time.time()
brojevi.sort()
after = time.time()
print(after- now)
