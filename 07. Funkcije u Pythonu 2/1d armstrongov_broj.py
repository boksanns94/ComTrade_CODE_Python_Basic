# domaci zadatak
# 153 = 1**3 + 5 **3 + 3**3  = 1 + 125 + 27 = 153
# 1634 = 1 ** 4 + 6 ** 4 + 3 ** 4 + 4**4 = 1 + 1296 + 81 + 256 = 1634

# sumiramo cifre stepenovane na broj cifara inicijalnog broja 

def prebroj_cifre(broj):
    if broj < 0:
        broj = -broj 
    
    brojac = 0
    while broj > 0:
        brojac+=1
        broj //= 10
    
    return brojac
# napisati funkciju koja za neki broj vraca armstrongovu sumu tog broja
def armstrongova_suma(broj):
    suma = 0 
    if broj < 0:
        broj = -broj
    broj_cifara = prebroj_cifre(broj)
    #print(broj_cifara)
    while broj > 0:
        poslednja = broj % 10
        broj //=10
        #broj_cifara = prebroj_cifre(broj) # ne moze da bude unutar petlje jer 
        # se promenljiva broj menja iz ponavljanja u ponavljanje petlje 
        # tj smanjuje mu se broj cifara 
        suma = suma + poslednja ** broj_cifara
        #print(suma)
    
    return suma
def da_li_je_armstrongov(broj):
    # if broj == armstrongova_suma(broj):
        # return True
    # else:
        # return False
    return broj == armstrongova_suma(broj)
def maksimum_armstrongove_sume(brojevi):
    trenutni_max_arms_suma = armstrongova_suma(brojevi[0])
    broj_koji_ima_najvecu_sumu = brojevi[0]
    for broj in brojevi:
        trenutna_arms_suma = armstrongova_suma(broj) # racunamo sumu armstrongovu 
        # za neki element iz liste, gde je broj trenutna vrednost iz liste ( uzima redom vrednosti
        # od pozicije 0 pa nadalje)
        if trenutna_arms_suma > trenutni_max_arms_suma:
            trenutni_max_arms_suma = trenutna_arms_suma
            broj_koji_ima_najvecu_sumu = broj
    return trenutni_max_arms_suma, broj_koji_ima_najvecu_sumu

# def iscrtaj_sablon(dimenzija, slovo):
    # if slovo == "a":
        # crtamo sablon za a
    # elif slovo == "b":
        # sablon za b
    # else:
        # sablon za jelkicu
    # if len(slovo) == 1:  
        # if slovo in "aqwertyuiopasdjksdhflklzxcvbnm":
            # da li je slovo u skupu

print(prebroj_cifre(12345))
print(armstrongova_suma(153))
print(armstrongova_suma(1634))

arms_brojevi = [] 
trenutni_test_broj = 10

while len(arms_brojevi) < 7:
    if da_li_je_armstrongov(trenutni_test_broj):
        #print(trenutni_test_broj,end=" ")
        arms_brojevi.append(trenutni_test_broj)
    trenutni_test_broj+=1
print(arms_brojevi)

brojevi = [3,5,11,23,123]
maks,broj_koji_je_maks = maksimum_armstrongove_sume(brojevi)
print(maks,broj_koji_je_maks)
def slovo_a(n):
    for i in range(n):
        if i == 0:
            print(" " + (n-2) * "*" + " ")
        elif i == n//2:
            print("*" * n)
        else:
            print("*" + " " * (n-2) + "*")
slovo_a(20)

def par_nepar(broj):
    lista_cifara = []
    broj = abs(broj)
    while broj > 0:
        poslednja = broj % 10
        broj //= 10
        lista_cifara.append(poslednja)
    print(lista_cifara)
    
    
    n = len(lista_cifara)
    for i in range(n-1):
        # if (lista_cifara[i] % 2 == 0 and lista_cifara[i+1] % 2 == 0) or (lista_cifara[i] % 2 != 0 and lista_cifara[i+1] % 2 != 0):
        #if lista_cifara[i] % 2 == lista_cifara[i+1] % 2:
        if (lista_cifara[i] + lista_cifara[i+1]) % 2 == 0:
            return False
    return True

        