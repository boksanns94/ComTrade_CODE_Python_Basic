# Napisati program koji rekurzivno ispisuje neki broj unapred i unazad
# 12345 -> 12345
# 12345 -> 54321

def broj_unapred_rekurzivno(broj):
    if broj == 0:
        return
    broj_unapred_rekurzivno(broj//10)
    print(broj%10, end="")

def broj_unazad_rekurzivno(broj):
    if broj == 0:
       return
    print(broj%10, end="")
    broj_unazad_rekurzivno(broj//10)



# Main

n = int(input("Unesite broj: "))
broj_unapred_rekurzivno(n)