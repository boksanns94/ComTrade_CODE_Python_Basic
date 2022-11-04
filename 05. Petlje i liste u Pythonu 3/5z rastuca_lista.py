# korisnik unosi n, a zatim i n celih brojeva u listu.
# ispitatai da li je lista rastuca (neopadajuca)

# 1 2 3 4 5 -> rastuca lista i neopadajuca lista
# 1 1 2 3 4 -> neopadajuca lista, koja nije rastuca

# 0 1 2 3 4
# 5 7 8 9 9
#  i      i+1
# [0] <= [1]
# [1] <= [2]
# [2] <= [3]
# [3] <= [4]

# i se krece do predposlednjeg elementa 
# ako se makar jednom desi da je trenutni element na poziciji i 
# veci od sledeceg elementa na poziciji i+1 
# onda lista vise nije neopadajuca

# koristimo algoritam sa pretpostavkom, pretpostavimo da je neopadajuca lista
# ako se makar jednom desi da nije -> menjamo flag na false i iskacemo iz petlje 
n = int(input("Unesite ceo broj:"))
brojevi = []
for i in range(n):
    unos = int(input("Unesite broj u listu:"))
    brojevi.append(unos)
print(brojevi)
pretpostavka_da_je_neopadajuci = True
for i in range(n-1): # i uzima sve pozicije od 0 do n-2 
    if brojevi[i] > brojevi[i+1]:
        pretpostavka_da_je_neopadajuci = False
        # print("Nije")
        # exit()
        
        break
# print("jeste")
#if USLOV: -> if True ili False
if pretpostavka_da_je_neopadajuci:
    print("Jeste")
else:
    print("Nije")
    

for i in range(n-1): # i uzima sve pozicije od 0 do n-2 
    if brojevi[i] > brojevi[i+1]:
        pretpostavka_da_je_neopadajuci = False
        print("Nije")
        # exit()
        
        break
else:
    print("Jeste")
    
