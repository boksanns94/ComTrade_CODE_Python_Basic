# funnkcija za prost broj
# napisati funkciju koja kao argument prima neki broj
# i proverava da li je on prost funkcija vraca True ako jeste,False ako nije 

def prost(broj): 
    for i in range(2,broj//2+1):
        if broj % i == 0:
            return False
    
    return True
# ispisati sve proste brojeve manje od 1000
print(prost(11))

for i in range(1,101):
    if prost(i):
        print(i,end=" ")

