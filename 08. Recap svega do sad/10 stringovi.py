tekst = "danas je cetvrtak"
for karakter in tekst:
    print(id(karakter),end=" ")

# print(tekst[1:5])
print()
print(id(tekst))
print(tekst[0])
#tekst[4] = "q"
print(tekst)
tekst = tekst[:4] +"q"+ tekst[5:]
print(tekst)

novi_tekst = ""
for i in range(len(tekst)):
    if i == 4:
        novi_tekst += "q"
    else:
        novi_tekst += tekst[i]
print(novi_tekst)

tekst = tekst.upper() # vraca novi string sa velikim slvoima
print(tekst)
