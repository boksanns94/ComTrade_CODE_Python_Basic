# 1234 -> 4 3 2 1
# 4 -> 123 
# 3 -> 12 
# 2 -> 1
# 1 -> 0
# 0 -> ne stampam nista

def unazad_rek(broj):
    if broj == 0:
        return
    print(broj%10,end=" ")
    unazad_rek(broj//10)
unazad_rek(1234)
print()
def ispis_unapred_rek(broj):
    if broj == 0:
        return
    
    unazad_rek(broj//10)
    print(broj%10,end=" ")
ispis_unapred_rek(1234)
print()


# 1234 -> 4 + suma(123)
# 123  -> 3 + suma(12)
# 12   -> 2 + suma(1)
# 1    -> 1 + suma(0)
# 0    ->     0
def suma_cifar(broj):
    if broj == 0:
        return 0
    return broj%10 + suma_cifar(broj//10)
print(suma_cifar(1234))