
from random import randint
broj = randint(0,2**30)
print(broj)

# 64 
# zamisljeni broj je manji od mog broja ja mogu da otpisem sve brojeve koji su veci od 64
# 0 64
# 32 
# 0-32
# 16 broj je veci od 16 mozemo da otpisemo sve brojeve manje od 16 
# 16 - 32
# 24 otpisujemo vece
# 16-24
# 20 - otpisujemo vece od 20
# 16 - 20
# 18
# 17
print(2**30)
donja_granica = 0
gornja_granica = 2**30
brojac = 0
while True:
    pokusaj = (donja_granica + gornja_granica) // 2
    if pokusaj == broj:
        print("Bravo pobedio sam,resenje je",pokusaj)
        print(brojac)
        exit(1)
    elif pokusaj < broj:
        donja_granica = pokusaj + 1
    else:
        gornja_granica = pokusaj - 1
    brojac+=1
    print(f"Opseg koji mi je preostao {donja_granica} - {gornja_granica} sledeci pokusaj je {(donja_granica + gornja_granica) // 2}")
