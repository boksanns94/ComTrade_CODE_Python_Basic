# Zadatak: Sa standardnog ulaza učitati vrednost i smestiti u
# promenljivu moja_promenljiva, potom na standardni izlaz odštampati
# vrednost koja je smeštena u moja_promenljiva i vrednost koja je
# smeštena u MOJA_PROMENLJIVA.

moja_promenljiva = input("Unesite vrednost:")
print(moja_promenljiva)
#print(MOJA_PROMENLJIVA) #izbacuje gresku jer nije definisana promenljiva MOJA_PROMENLJIVA

#Zadatak: Napisati program koji zamenjuje vrednosti dvema
# promenljivama koje korisnik unosi.

prvi_broj = int( input("Unesite broj:")) # 10
drugi_broj = int(input("Unesite drugi broj:")) # 5
print("POCETNE VREDNOSTI")
print("Vrednost prve:",prvi_broj)
print("Vrednost druge:",drugi_broj)
print()
pomocna = prvi_broj # pomocna -> 10
prvi_broj = drugi_broj # prvi_broj -> 5
drugi_broj = pomocna # drugi_broj -> 10
# prvi_broj = drugi_broj #  prvi_broj -> 5
# drugi_broj = prvi_broj # drugi_broj = 5 NECE RADITI KAKO TREBA
print("POSLE PRVE ZAMENE")
print("Vrednost prve:",prvi_broj)
print("Vrednost druge:",drugi_broj)
print()

# visestruka dodela vrednosti 
prvi_broj, drugi_broj = drugi_broj, prvi_broj 
# mora da postoji isti broj promenljivih sa leve i desne
print("POSLE DRUGE ZAMENE")
print("Vrednost prve:",prvi_broj)
print("Vrednost druge:",drugi_broj)
print()