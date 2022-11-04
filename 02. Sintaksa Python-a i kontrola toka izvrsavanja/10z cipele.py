# Korisnik unosi koliko pari cipela zeli da kupi
# u zavisnosti od kolicine pari cipela koje kupuje,
# cena je razlicita
# 1-9 -> 12$ komad
# 10-99 -> 10$ komad
# 100+ -> 7$ komad
# ako je negativan broj cipela, ispisati poruku GRESKA!!
# 7 -> 84$, 11 -> 110$, 110 -> 770$, -1 -> GRESKA

broj_pari_cipela = int(input("Unesite koliko cipela zelite:"))

if broj_pari_cipela < 1:
    print("Greska")
    exit() # exit je funkcija koja zavrsava rad programa
elif broj_pari_cipela >= 1 and broj_pari_cipela <=9:
    cena = 12 * broj_pari_cipela
elif broj_pari_cipela >= 10 and broj_pari_cipela <= 99:
    cena = 10 * broj_pari_cipela
else:
    cena = 7 * broj_pari_cipela

print(f"Ukupna cena je {cena}$ za {broj_pari_cipela} cipela")

if broj_pari_cipela < 1:
    print("Greska")
    exit() # exit je funkcija koja zavrsava rad programa
elif broj_pari_cipela <=9:
    cena = 12 * broj_pari_cipela
    
elif broj_pari_cipela <= 99:
    cena = 10 * broj_pari_cipela
else:
    cena = 7 * broj_pari_cipela

print(f"Ukupna cena je {cena}$ za {broj_pari_cipela} cipela")



