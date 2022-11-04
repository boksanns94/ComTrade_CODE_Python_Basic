# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 23:22:17 2021

@author: Boksan
"""

# Napisati funkciju koja ce kao argument da primi dve vrednosti, dimenziju sablona i slovo.
# Obezbediti da se u zavisnosti od prosledjenog slova ispisuje odgovarajuci sablon.
# Moguca slova su a,b,c,d,e,f. U slucaju da nije prosledjeno neko od ovih slova iscrtati
# jelkicu dimenzije n. Jelkica je od *, kao i slova.

# na dnu koda ima deo koji sam koristio da testiram sva slova automatski
# zato sam importovao time modul, kako bi mogao mi bilo lakse da pratim ispis
# import time

def stampaj_jelkicu(n:int) -> None:
    for i in range(n):
        print(f"{(2*i-1)*'*':^{2*n-1}}")
    print(f"{(n//2)*'|':^{2*n-1}}")

def vodoravna_linija(n:int) -> None:
    print(n*"*")

def jedna_zvezdica(n:int) -> None:
    for i in range(n):
        print("*")

def zvezdice_sa_razmacima(n:int) -> None:
    for i in range(n):
        print("*"+n*" "+"*")
    if n == 0:
        print("**")

def stampaj_slovo_a(n:int) -> None:
    vodoravna_linija(n+2)
    zvezdice_sa_razmacima(n)
    vodoravna_linija(n+2)
    zvezdice_sa_razmacima(n)

def stampaj_slovo_b(n:int) -> None:
    vodoravna_linija(n)
    zvezdice_sa_razmacima(n-1)
    vodoravna_linija(n)
    zvezdice_sa_razmacima(n-1)
    vodoravna_linija(n)

def stampaj_slovo_c(n:int) -> None:
    print(" ",end="")
    vodoravna_linija(n)
    jedna_zvezdica(n)
    print(" ",end="")
    vodoravna_linija(n)

def stampaj_slovo_d(n:int) -> None:
    vodoravna_linija(n)
    zvezdice_sa_razmacima(n-1)
    vodoravna_linija(n)

def stampaj_slovo_e(n:int) -> None:
    vodoravna_linija(n+1)
    jedna_zvezdica(n) 
    vodoravna_linija(n+1)
    jedna_zvezdica(n) 
    vodoravna_linija(n+1)

def stampaj_slovo_f(n:int) -> None:
    vodoravna_linija(n+1)
    jedna_zvezdica(n) 
    vodoravna_linija(n+1)
    jedna_zvezdica(n)

def izbor_stampe_slova(slovo:str, n:int) -> None:
    if slovo == 'a' or slovo == 'A':
        stampaj_slovo_a(n)
    elif slovo == 'b' or slovo == 'B':
        stampaj_slovo_b(n)
    elif slovo == 'c' or slovo == 'C':
        stampaj_slovo_c(n)
    elif slovo == 'd' or slovo == 'D':
        stampaj_slovo_d(n)
    elif slovo == 'e' or slovo == 'E':
        stampaj_slovo_e(n)
    elif slovo == 'f' or slovo == 'F':
        stampaj_slovo_f(n)
    else:
        stampaj_jelkicu(n)

unos_slova = input("Unesite slovo za stampu: ")
unos_dimenzije = int(input("Unesite dimenziju slova: "))
izbor_stampe_slova(unos_slova, unos_dimenzije)

# =============================================================================
# # ovaj deo sam koristio za test svih simbola kao i stampe jelkice
# # da ne bi morao rucno jedan po jedan scenario da testiram
#
# slova = ["a","A","b","B","c","C","d","D","e","E","f","F","x",1,"yy",000,"foo","bar",-5]
# dimenzije = [1,2,3,4,5,6]
# for slovo in slova:
#     for dimenzija in dimenzije:
#         izbor_stampe_slova(slovo, dimenzija)
#         time.sleep(0.5)
# =============================================================================