# pdf4_zad5

lista_slova = []
n = int(input("Unesite broj slova koji zelite u listi:"))
recenica = "danas"
print(recenica[2])
print(len(recenica))
while len(lista_slova) < n:
    slovo = input("Unesite slovo:")
    if len(slovo) == 1:
        lista_slova.append(slovo)
# da li se uz pomoc unetih slova moze zapisati rec Zima
print(lista_slova)

if "Z" in lista_slova and "i" in lista_slova and "m" in lista_slova and "a" in lista_slova:
    print("Moze da se sastavi rec Zima")
else:
    print("Ne moze da se sastavi rec Zima")
    
# Kako da nadogradimo ovo ako zelimo da ovo moze da radi za svaku rec koju npr 
# korisnik unese. 
# ( dozvoljeni su duplikati slova iz unete liste )
# [m,a,t,e,i,k] -> matematika
trazena_rec = input("Koju rec trazite:")

# da bismo mogli da zapisemo neku rec, mora svako slovo te reci 
# da bude u listi slova. 
# ako se makar jednom desi, da neko slovo nije u listi slova
# onda nije moguce zapisati tu rec.
pretpostavka_da_moze_da_se_zapise = True # pretpostavimo da moze da se zapise

for slovo in trazena_rec: # trazimo neki primer koji nam rusi pretpostavku
# prodjemo kroz sva slova koja su u trazenoj reci
# ako se neko od slova trazene reci ne nalazi u listi slova koja su nam zadata
    if slovo not in lista_slova:
        print(slovo,"se ne nalazi u listi slova",lista_slova)
        pretpostavka_da_moze_da_se_zapise = False # menjamo pretpostavku na false
        break # iskacemo iz petlje 
if pretpostavka_da_moze_da_se_zapise: # i nakon toga proveravamo vrednost flaga
    print("Moze da se napise",trazena_rec)
else:
    print("Ne moze da se zapise",trazena_rec)


