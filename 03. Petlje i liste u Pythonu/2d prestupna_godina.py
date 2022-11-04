# prestupna godina
# godina je prestupna ako je deljiva sa 4 i nije deljiva sa 100
# ILI ako je deljiva sa 400
# 2004 -> prestupna
# 2000 -> prestupna
# 1900 -> nije prestupna zato sto je deljiva sa 4 i deljiva je sa 100

godina = int(input("Unesite godinu:"))

if (godina % 4 == 0 and godina % 100 != 0) or godina % 400 == 0:
    print(f"{godina} je prestupna")
else:
    print(f"{godina} nije prestupna")
    

    