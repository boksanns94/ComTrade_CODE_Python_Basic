# Deklaracija funkcija 

# sve funkcije se deklarisu sa kljucnom reci def 

# def naziv_funkcije(opciono: argumenti funkcije u formatu arg1,arg2...):
    # telo funkcije 
    
# Napisati funkciju koja ce samo da ispise Hello World
def pozdravi():
    print("Hello world")
    
# poziva se tako sto kazemo 
# naziv_funkcije(argumenti istim redosledom kao sto je zadato u funkciji)
print("Komande pre funkcije")
pozdravi()
print("Komande posle funkcije")

def pozdravi_me(ime):
    global moje_ime
    print("Hello ime",ime)
    print("Hello moje_ime",moje_ime)
    moje_ime = "Izmenjeno ime"
moje_ime = "Milan"
pozdravi_me("Dusan")

pozdravi_me(moje_ime)

print("Posle svih izmena:",moje_ime)

#print(ime)


    



    