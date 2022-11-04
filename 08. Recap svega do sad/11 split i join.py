
tekst = "danas je cetvr\ttak dan kada odma\nram"
# metoda split deli string po nekom karakteru i vraca listu stringovu 
# sa tim 'delimiterom'
# ako ne primi argument podrazumevano je to neki bilo koji beli znak
# sta su beli znaci: razmak tab ili novi red
tekst = "danas je cetvrtak dan kada odmaram"
x = tekst.split()
print(x)

# tekst = "python CODE programiranje CODE je CODE zanimljivo"
# x=tekst.split("CODE") # moze i bilo koji tekst da bude string po kome splitujemo
# print(x)
spojeno = " PYTHON ".join(x) # x mora da bude lista STRINGOVA!!
print(spojeno)

test = "ana banana"
print(test.count("ana"))

lista = ["a","n","a","ana"]
print(lista.count("ana"))

print(test.find("na")) # 1 
print(test.find("na",3)) # 6 drugi argument je opcioni i predstavlja prvu poziciju na kojoj je taj 
# string posle zadate pozicije ( ukljucena je i trojka)
print(test.find("na",3,8)) # treci argument je krajnji index na kome trazimo, i on NIJE ukljucen u opseg








