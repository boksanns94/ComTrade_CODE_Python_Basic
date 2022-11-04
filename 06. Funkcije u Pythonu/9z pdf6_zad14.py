# zad14 a,b,c,d

# a ) Napisatu funkciju koja računa kvadrat unetog broja
def kvadrat(broj):
    return broj * broj
# b) apsolutna vrednost |x| = pozitivan x 
def apsolutna_vrednost(broj):
    if broj < 0:
        broj = -broj
    return broj
    
    # if broj < 0 :
        # return -broj
    # else:
        # return broj
#c) kub nekog broja 
def kub(broj):
    return broj * broj * broj
# funkcija koja prima dve vrednost x i n,  x je broj koji stepenujemo, n je stepen na koji ga
# podizemo ne koristimo operator ** -> return x ** n
def stepenovanje(x,n):
    proizvod = 1 
    # 2**5 = 2*2*2*2*2 ( 5 puta mnozim dvojku samu sa sobom)
    # a**3 => a*a*a (3 puta)
    # a**b => a*a*a*a*a.... ( b puta ) 
    # x ** n -> x mnozim sam sa sobom n puta ( onoliko koliki je stepen )
    for i in range(n): # ova petlja se ponavlja za sve vrednosti i od 0 do n-1 
    # sto je ukupno n puta 
        proizvod = proizvod * x
    # for i in range(0): -> x:0,z:1,y:0 krecemo od x y nije ukljuceno u opseg
    # dakle nece se desiti nijednom petlja 
    return proizvod
print(kvadrat(5))
print(kub(5))
print(apsolutna_vrednost(-5))
print(apsolutna_vrednost(10))
print(apsolutna_vrednost(0))
print(stepenovanje(2,0))
