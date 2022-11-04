# 1234 -> 4 + 123 unazad 
# 123 unazad -> 3 + 12 unazad 
# 12 unazad -> 2 + 1 unazad 
# 1 unazad -> 1 i 0 unazad
def broj_unazad_rekurzivno(broj):
    if broj >= 0 and broj <10:
        print(broj)
        return 
    #else:
    poslednja_cifra = broj % 10
    print(poslednja_cifra,end=" ") # 4 3 2 
    broj_unazad_rekurzivno(broj//10)

def broj_unapred_rekurizvino(broj):
    print("Pozvana funkcija za ",broj)
    if broj >= 0 and broj <10:
        print("Stigao sam do kraja,sada ispisujemo poslednju cifru")
        print(broj,end=" ")
        return 
    
    broj_unapred_rekurizvino(broj//10)
    print("Ja sam docekao da se zavrsi rekurzija od ",broj//10)
    print(broj%10,end=" ")
print(broj_unazad_rekurzivno(1234))

broj_unapred_rekurizvino(1234)
    