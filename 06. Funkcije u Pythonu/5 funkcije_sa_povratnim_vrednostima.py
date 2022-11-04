# Funkcije koje vracaju neki rezultat 

def kolicnik(prvi,drugi):
    if drugi != 0:
        return prvi / drugi # return oznacava kljucnu rec 
        # koja nam govori da je vrednost pored return rezultat izvrsavanja 
        # te funkcije 
        # kada u funkciji naidjemo na komandu return
        # tu se zavrsava rad funkcije!!!
        print("caoooo")
    else:
        print("Greska,deljenje nulom nije definisano")
def pozdrav():
    print("Hello")
#kolicnik(20,4)
#20/4
print(kolicnik(20,4))

rez = kolicnik(10,4)
print(rez)

print(kolicnik(10,0))

print(pozdrav())
pozdrav()
        


