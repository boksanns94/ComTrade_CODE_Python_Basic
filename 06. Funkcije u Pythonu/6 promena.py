# izmena vrednosti promenljive 

def promeni_me(x):
    x = x + 1
    print(x)

def promeni_me_zaista():
    global x
    x = x + 1 
    
x=5 # x ima vrednost 5 u glavnom delu programa 
print(x,"pre funkcije") # 5 
promeni_me(x) # pozivamo funkciju promeni me kojoj prosledjujemo promenljivu x 
# 
print(x,"posle funkcije")

promeni_me_zaista() # prilikom poziva funkcije 
# MORATE DA IMATE ISTI BROJ argumenata pozicionih kao sto je navedeno u samoj 
# deklaraciji funkcije
print(x,"posle zaista promene")

rez = promeni_me(x)
print(rez)