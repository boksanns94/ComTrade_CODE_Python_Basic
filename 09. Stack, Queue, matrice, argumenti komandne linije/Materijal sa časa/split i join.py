# split prima neki string => list[str] razdvojenih po nekom delimiteru ( string )
tekst = "danas je ponedeljak"
reci = tekst.split(" ")
print(reci)
tekst = "Ponedeljak CODE utorak CODE petak sreda CODE tekst"
print(tekst.split("CODE"))

# join je inverzna operacija, join prima neku listu stringova i spaja ih po nekom znaku
reci = ["danas","je","ponedeljak"]
spojeno = ",".join(reci)
print(spojeno)
brojevi = [3,6,7,1,2,3,4] # -> 3,6,7....
brojevi_str = [ str(broj) for broj in brojevi ]
print(brojevi_str)
spojeno = ",".join(brojevi_str)
print(spojeno)