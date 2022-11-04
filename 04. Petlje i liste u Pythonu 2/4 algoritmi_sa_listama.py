# algoritmi sa listama 

# Korisnik unosi n, a zatim i n celih brojeva, popuniti listu tim brojevima i  ispisati sve elemente u toj listi.
# 5 
# Unesite 1. element: 10
# Unesite 2. element: 1
# Unesite 3. element: 2
# Unesite 4. element: 30
# Unesite 5. element: 40

# -> [10,1,2,30,40] 

n = int(input("Unesite duzinu liste:")) 
brojevi = [] # lista je na pocetku prazna, praznu listu definisemo sa [] 
for i in range(n): # petlja koja se ponavlja n puta 
    unos = int(input(f"Unesite {i+1}. broj:")) # u svakom prolasku kroz petlju trazimo od korisnika unos
    brojevi.append(unos) # ubacujemo taj unos u listu 
print(brojevi) # stampamo trenutno stanje u listi
# Zajednicko za sve ove algoritme je da cemo uvek imati neku promenljivu koja ce cuvati trenutni rezultat operacije 
# 1) trazenje zbira elemenata neke liste, kada trazimo zbir bice nam potreban neka promenljiva 
trenutni_zbir = 0 # u najgorem slucaju ova lista ce biti prazna, tako da je tada zbir svih elemenata 0 
# 0 je neutralna za sabiranje -> 0 + x = x 

# 6 7 1 2 3
# 1) pristup je prolazak kroz sve pozciije preko i in range
for i in range(n):
    trenutni_zbir = trenutni_zbir + brojevi[i] # svaki put kada trazimo zbir, mi staru vrednost zbira uvecavamo za tu 
    # neku vrednost koju zelimo da dodamo u zbir, s obzirom da mi dodajemo SVE ELEMENTE LISTE -> mi cemo svaki element da dodamo
    #print(f"Trenutni zbir posle {i+1}. elementa liste:",trenutni_zbir)
print("Zbir svih elemenata u listi je:",trenutni_zbir)
trenutni_zbir_parnih = 0
# 2) prolazak kroz listu koriscenjem privremene promenljive 
for broj in brojevi:
    if broj % 2 == 0: # provera da li je paran, da li je ostatak pri deljenju sa 2 jednak 0
        trenutni_zbir_parnih = trenutni_zbir_parnih + broj
        #print(trenutni_zbir_parnih)
print("Zbir parnih elemenata liste:",trenutni_zbir_parnih)

# 2) Algoritam kada zelimo da prebrojimo koliko puta se nesto desilo, tada zelimo da imamo neku pomocnu promenljivu u kojoj ce biti trenutni rezultat
brojac = 0
# koliko elemenata u ovom nizu je vece od elementa na poziciji 1 
for broj in brojevi: # prolazak kroz celu listu 
    if broj > brojevi[1]: # proverava da li je broj veci od pozicije 1 u nizu
        brojac = brojac + 1  # ako jeste brojac se uvecava za 1 
print("Brojac je na kraju:",brojac) # i na kraju posle petlje stampamp rezultat 

# 3) Trazenje proseka liste -> 
# Za njega nam je potreban zbir svih elemenata i koliko ih ima 
zbir_za_prosek = 0
brojac_za_prosek = 0
# ako trazite prosek cele liste -> onda mozete samo da imate zbir -> prosek = zbir / len(lista) 
# ako se trazi koliki je prosek pod nekim uslovom u listi

# npr pronadji prosek neparnih elemenata u listi.
# 6
# 3 3 7 4 4 0
for broj in brojevi: # prolazimo kroz celu listu
    if broj % 2 != 0: # pitamo da li je trenutni element adekvatan, da li ispunjava uslov iz zadatka 
        brojac_za_prosek = brojac_za_prosek + 1  # ako jeste dobar, uvecavamo brojac 
        # brojac_za_prosek += 1
        # brojac_za_prosek /= 5     <=> brojac_za_prosek = brojac_za_prosek / 5 
        zbir_za_prosek = zbir_za_prosek + broj  # uvecavamo zbir 
if brojac_za_prosek != 0:
            
    prosek_neparnih = zbir_za_prosek / brojac_za_prosek
    print("Prosek neparnih elemenata liste je:",prosek_neparnih)
else:
    print("Nema nijedan neparan element")