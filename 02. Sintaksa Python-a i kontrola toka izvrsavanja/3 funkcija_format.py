# funkcija format

a=5
b=10.3
c=15.556362
zbir = a+b+c
# 5 + 10.3 + 15.55632 = .... 
print(a,"+",b,"+",c,"=",zbir)
#                                     0,1,2, 3
print( "{3} + {1} + {2} = {0}".format(a,b,c,zbir))
# unutar {} mozemo imati zapis na sledeci nacin
# poziciju argumenta iz formata koju zelimo da stavimo na to mesto
# pozicije u programiranju krecu uvek od 0

# predstavljanje decimalnog broja na nekom broju decimala
print("{:^10.2f} tekst".format(c)) # formatiramo na 2 decimale
# levo od dvotacke je "pozicija argumenta" u zagradama nakon formata
# a desno mozemo da zapisemo vise stvari
# < > ^ - poravnanje levo, desno i centar
# 10 - ukupan broj mesta koji podataka zauzima
# .2 - broj decimala koje se prikazuju
# f d c s - tip podatka koji se stampa
print("{0:<10d} + {1:<.2f} + {2:<10.2f} = {3}".format(a,b,c,zbir))


# f - stringovi oni imaju prefix f pre samog stringa 
# i ponasaju se kao obican string, samo sto na mestima gde bismo zeleli
# da ispismo vrednost promenljive {naziv_promenljive}

print(f"{a} + {b} + {c:<10.2f} = {zbir}")
# {naziv_promenljive : pozicioniranje, ukupan broj mesta, .broj_decimala}
# pozicioniranje 
# < - lepi ispis za levu ivicu
# > - za desnu ivicu
# ^ - centrira sadrzaj 
# ukupan broj mesta -> koliko ce mesta zauzeti MINIMALNO taj broj zajedno sa decimalama
# .broj_decimala -> na koliko decimala zaokruzujete broj
# f -> float 
# d -> int
# s -> string
# c -> character

# Ć = 5 # MOZE OVO RADI,ALI NIJE PREPORUKA!!
# print(Ć)