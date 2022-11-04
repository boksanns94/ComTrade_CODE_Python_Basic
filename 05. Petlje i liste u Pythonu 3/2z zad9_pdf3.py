# Napisati program koji učitava ceo broj i ispisuje njegove cifre u obrnutom poretku.

broj = int(input("Unesite ceo broj:"))
negativan_broj = False
if broj < 0:
    broj = -broj
    negativan_broj = True
# 1234 % 10 = 4 
# 1234 : 10 = 123(4), 1234 // 10 = 123, 1234 % 10 = 4
# 123  : 10 =  12(3), 123  // 10 = 12 , 123  % 10 = 3
# 12   : 10 =   1(2), 12   // 10 = 1  , 12   % 10 = 2
# 1    : 10 =   0(1), 1    // 10 = 0  , 1    % 10 = 1
if negativan_broj:
    print("-",end="")
while broj > 0:
    poslednja_cifra = broj % 10  # uzimamo trenutnu poslednju cifru broja
    broj = broj // 10 # broj umanjujemo 10 puta, da bismo izgubili tu poslednju cifru
    print(poslednja_cifra,end=" ")
    
# broj = input("Unesite broj:") 
# print(broj[::-1])
