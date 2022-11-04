
brojevi = [3,4,1,2,3]
print(brojevi.sort()) # ne vraca nista,ALI vrsi izmenu ( nista = None )
print(brojevi)

brojevi = [3,4,1,2,3]
brojevi = sorted(brojevi) # funkcija sorted NE MENJA LISTU KOJA JOJ JE PROSLEDJENA,
# vec vraca NOVU listu, koja je sortirana 
print(brojevi)
#print("asd")

gradovi = ["beograd","nis","BEOGRAD","KRALJEVO","valjevo","NOVI sad"]
gradovi.sort()
print(gradovi)

print(ord('a'))
print(ord('Ћ'))

print(chr(100))