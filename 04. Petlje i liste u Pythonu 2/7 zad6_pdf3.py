# zad6_pdf3
# Napisati program koji učitava realan broj x i ceo nenegativan broj n i izračunava n
# ti stepen broja x. U slučaju neispravnog unosa ispisati odgovarajuću poruku o
# grešci. Zadatak rešiti bez korišćenja aritmetičkog operatora **.

x = float(input("Unesite neki realan broj:"))
n = int(input("Unesite stepen na koji podizete broj:")) 

# if n < 0:
    # print("Greska!")
    # exit()
    
# stepenovanje predstavlja proizvod 
# 2 ** 5 = 2*2*2*2*2 ( 5  puta pomnozio dvojku samu sa sobom )
# a ** 3 = a*a*a ( a sam pomnozio sa sobom, 3 puta)
# a ** b = a*a*a*a ..... *a (  a sam pomnozio sa sobom, b puta )

# proizvod = 1 # stepenovanje je proizvod u sustini, zato proizvod krece od 1 
# for i in range(n):
    # proizvod = proizvod * x # svaki put stari proizvod mnozimo sa osnovom 
# print(f"{x} ** {n} = {proizvod}") # pokusajte da doradite ovaj zadatak da radi i sa negativnim stepenim 

# 2 ** 3 = 8
# 2 ** -3 = 1 / (2**3) = 1/8 = 0.125
proizvod = 1 # zato sto je stepenovanje mnozenje 
da_li_je_negativan_stepen = False # pretpostavimo da nije negativan stepen
if n<0: # ako jeste negativan stepen
    da_li_je_negativan_stepen = True  # menjamo ovu promenljivu na True
    n = -n # -3 -> 3  # stepen menjamo sa negativnog na pozitivan, da bi ova nasa for petlja mogla da se izvrsi
    # for i in range(-3) -> se ne desava nijednom
    # for i in range(3) -> ce se ponoviti 3 puta 
    
for i in range(n):
    proizvod = proizvod * x # racunamo rezultat
    
if da_li_je_negativan_stepen == True: # ako je stepen negativan 
    print(1/proizvod) # stampamo reciprocnu vrednost 1 / proizvod 
else:
    print(proizvod) # ako nije negativan stepen onda stampamo samo taj proizvod





    
