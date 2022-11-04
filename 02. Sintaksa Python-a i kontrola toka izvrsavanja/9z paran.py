#Zadatak: Uneti broj sa standardnog
#ulaza i ispisati da li je broj paran

broj = int(input("Unesite neki broj:"))
# kada je broj paran? kada je deljiv sa 2
# kada je deljiv sa 2?
ostatak = broj % 2
if ostatak == 0:
    print(broj,"je paran")
else:
    print(broj,"je neparan")
    
if broj % 2 ==0:
    print(broj,"je paran")
else:
    print(broj,"je neparan")