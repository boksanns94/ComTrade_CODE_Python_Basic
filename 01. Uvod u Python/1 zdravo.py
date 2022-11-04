
# Linije koje pocinju sa znakom # predstavljaju KOMENTARE
# komentari predstavljaju deo koda koji se racunar 
# ignorise prilikom pokretanja programa

print("Hello world")
# print je funkcija koja nam omogucava da ispisemo neki tekst
# na standardni izlaz, sam tekst ako zelimo da se prenese
# tacno onako kako je zapisan je potrebno zapisati ili 
# pod jednostrukim ili dvostrukim navodnicima

# ctrl + s -> save 
# ctrl + n -> new file
# svi pajton fajlovi imaju extenziju .py !!!
# i obavezno svi fajlovi da bismo mogli da ih pokrenemo
# moraju biti .py 
# desni klik na tab gde je naziv fajla 
# -> open containing folder in cmd 
# -> da bismo pokrenuli fajl treba da pokrenemo komandu
# py naziv_fajla.py 

print('Hello world again')

print("Hello")

print("Dusan Sijacic\nVenizlosova 1")

# escape karakteri su karakteri koje nije moguce zapisati
# u samom tekstu unutar navodnika, a da ne poremetimo sintaksu
# samog jezika 
# vecina escape karaktera pocinje sa znakom \ ( slovo ž na srpskoj latinicnoj tastaturi )
# \n - predstavlja oznaku za novi red 
# \t - oznacava oznaku za tabulator
# \" = "
# \' = '

print("Isao sam u \"OS Mihalo Petrovic Alas\"",end=" CODE ")
print('Isao sam u "OS Mihailo Petrovic Alas"')

# print podrazumevano dodaje znak za novi red na kraj ispisa
# to mozemo da promenimo tako sto dodamo jos jedan 
# atribut koji se naziva end, end menja znak za kraj printa
# na tekstualni podatak koji mu je dodeljen

print("Dusan","Sijacic","Venizelosova 1","Stari Grad")
print("Dusan","Sijacic","Venizelosova 1","Stari Grad",sep=",")
# atribut sep=" string izmedju ispisa umesto znaka razmak"

print("Hello" + "World")  # sabiranje izmedju tekstova
# rezultat je njihov tekst spojen

print(123)
print("Moj omiljeni broj je", 123 )
# ako zelimo da uz pomoc printa ispisemo razlicite tipove
# tekst i brojeve, moramo da ih razdvojimo zarezima.
print(2*10) # unutar printa moze biti izracunata i neka
# matematicka operacija

print(" \"Hej, dodji ovamo\" ")

print("2 + 2 = 4")
print("2 + 2 =", 2+2)

print("Ovo je #pocetak komentara")

