# aritemticki operatori

# Korisnik unosi dva cela broja, prvi i drugi, 
# izracunati i ispisati lepo formatirano sve matematicke operacije 

prvi = int(input("Unesite prvi broj:"))
drugi = int(input("Unesite drugi broj:"))

print(prvi,drugi)

# operacije koje su iste kao i u matematici su - + * 
zbir = prvi + drugi
# 10 15 -> 10 + 15 = 25
print(prvi,"+",drugi,"=",zbir)
razlika = prvi - drugi
print(prvi,"-",drugi,"=",razlika)
proizvod = prvi * drugi
print(prvi,"*",drugi,"=",proizvod)

# operatori za deljenje 
# /    - kao rezultat uvek vraca decimalan broj! 6 / 2 = 3.0
# //   - rezultat celobrojnog deljenja -> 10 // 4 = 2 
# %    - ostatak pri celobrojnom deljenju -> 10 % 7 = 3
# 10 : 7 = 1(3)
decimalno = prvi / drugi 
celobrojno = prvi // drugi
ostatak = prvi % drugi


print(prvi,"/",drugi,"=",decimalno)
print(prvi,"//",drugi,"=",celobrojno)
print(prvi,"%",drugi,"=",ostatak)
print(prvi,":",drugi,"=",celobrojno,"(",ostatak,")",sep="")

# ** - operator za stepenovanje 
print(2**10)



