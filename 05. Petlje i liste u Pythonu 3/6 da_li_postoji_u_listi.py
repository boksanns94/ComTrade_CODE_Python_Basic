# data je lista brojeva, proveriti da li se neki uneti broj nalazi u listi
# bez koriscenja operatora in.

brojevi = [3,4,5,1,2,123]

trazeni_broj = int(input("Unesite broj koji trazite u listi:"))

da_li_je_broj_u_listi = False

for broj in brojevi:
    if broj == trazeni_broj:
        da_li_je_broj_u_listi = True
        break

if da_li_je_broj_u_listi:
    print(trazeni_broj,"je u",brojevi)
else:
    print(trazeni_broj,"nije u",brojevi)