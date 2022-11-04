# Korisnik unosi dva broja
# ispitati koji broj ima veci prosek cifara 

prvi = int(input("Unesite prvi broj:"))
drugi = int(input("Inesite drugi broj:"))
kopija1 = prvi
kopija2 = drugi
suma_1 = 0
brojac_1 = 0

while prvi > 0:
    poslednja_cifra = prvi % 10 
    prvi = prvi // 10
    suma_1 = suma_1 + poslednja_cifra
    brojac_1 = brojac_1 + 1 
prosek_1 = suma_1 / brojac_1 
suma_2 = 0 
brojac_2 = 0
while drugi > 0 :
    poslednja_cifra = drugi % 10
    drugi = drugi // 10
    suma_2 = suma_2 + poslednja_cifra
    brojac_2 = brojac_2 + 1
prosek_2 = suma_2 / brojac_2
print(prosek_1,prosek_2)
if prosek_1 > prosek_2:
    print(f"{kopija1} ima veci prosek {prosek_1}")
elif prosek_1 < prosek_2:
    print(f"{kopija2} ima veci prosek {prosek_2}")
else:
    print(f"Proseci su jednaki {prosek_1}")