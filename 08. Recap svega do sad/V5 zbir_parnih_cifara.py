# Napisati program koji rekurzivno racuna zbir parnih cifara u broju.
# 123456 = 2+4+6
# 6 + 12345 broj%10 + broj//10
# 5 + 1234
# 4 + 123
# 3 + 12

def rekurzivno_suma_parnih_cifara(broj):
    if broj == 0:
        return 0
    if (broj%10) % 2 == 0:
        return broj%10 + rekurzivno_suma_parnih_cifara(broj//10)
    else:
        return 0 + rekurzivno_suma_parnih_cifara(broj//10)



# Main

n = int(input("Unesite broj: "))
print(f"Suma parnih cifara broj {n} je {rekurzivno_suma_parnih_cifara(n)}.")