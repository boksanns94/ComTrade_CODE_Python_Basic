# profesor unosi broj poena ostvarenih na nekom ispitu na fakultetu
# proveriti da li je student polozio ispit i sa kojom ocenom
# 0-50 5
# 51-60 6 
# 61-70 7 
# 71-80 8 
# 81-90 9 
# 91-100 10
# <0  >100 -> los unos

broj_poena = int(input("Unesite ceo broj:"))

# provera da li je ocena 6
# da bi ocena bila 6, mora da ima izmedju 51 i 60 
#if 51 <= broj_poena <= 60: # moguce u pajtonu u drugim jezicima ne
if broj_poena >= 51:
    if broj_poena <= 60:
        print("Ocena 6")
    else:
        print("Nije ocena 6, imate vise od 60 poena")
else:
    print("Nije ocena 6,imate ispod 51 poen")
    
# logicki operatori su operatori koji mogu da se vezu izmedju 2 ili vise
# logickih uslova
# 1) Logicko i ( AND ) 
# TABELA ISTINITOSTI za logicko and 0 - netacno 1 - tacno
# if USLOV1 and USLOV2: 

# USLOV1        USLOV2      USLOV1 and USLOV2
#   0               0           0
#   0               1           0
#   1               0           0
#   1               1           1
# logicko i je tacno AKO I SAMO AKO 
# su oba uslova (svi uslovi) koji su vezani sa logickim i TACNI!!
if broj_poena >= 51 and broj_poena <=60:
    print("Ocena 6")
else:
    print("Nije ocena 6")
    
#LOGICKO ILI ( or )
# TABELA ISTINITOSTI za logicko or 0 - netacno 1 - tacno
# if USLOV1 or USLOV2: 

# USLOV1        USLOV2      USLOV1 or USLOV2
#   0               0           0
#   0               1           1
#   1               0           1
#   1               1           1 
# LOGICKO ili je tacno u celini ako je MAKAR jedan od uslova tacan
# ( ILI jedan ILI drugi)
if broj_poena < 0 or broj_poena > 100:
    print("Los unos, mora biti od 0 do 100")
    
# 3) logicki operator not 
# on samo negira vrednost nekog uslvoa
# uslov1        not uslov1  
#   0               1
#   1               0
    
    


    