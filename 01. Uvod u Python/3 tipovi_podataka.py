# tipovi podataka u pythonu su 
# 1) integer  - celi brojevi
# 2) float - decimalni brojevi,brojevi sa decimalnim zarezom
# 3) string  - tekstualni tip podatka 
# 4) boolean - logicki tip podatka koji moze uzimati samo vrednosti
# tacno ili netacno True ili False
# 5) NoneType - None -> nedodeljenu vrednost u memoriji

broj = input("Unesite neki broj:")
print(broj * 3 )
# da bismo izvrsili konverziju ("castovanje") iz tipa u tip potrebno je da iskoristimo neku od ovih funkcija
# 1) integer -> int(naziv_promenljive)
# 2) float ->   float(naziv_promenljive)
# 3) string ->  str(naziv_promenljive)
# 4) boolean -> bool(naziv_promenljive)

broj = int(broj)
print(broj * 3)

broj = broj + 10
print(broj)

decimalni = input("Unesite neki decimalni broj:")
decimalni = float(decimalni)
print("Vrednost decimalnog broja je:",decimalni)

test = 100 
# print("Moj podatak je" + test) # bice greska jer je test tipa int 
test = str(test)
print("Moj podatak je" + test)

print("Dusan" + "Sijacic")
print("Dusan","Sijacic")


decimalni = float(input("Unesite neki decimalni broj:"))
print(decimalni * 3 )




