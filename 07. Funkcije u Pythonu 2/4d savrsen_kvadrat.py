# da bi neki broj bio savrsen kvadrat, on mora da bude zbir tacno 2 
# kvadrata sa kojim je deljiv ( sa ponavljanjima)
# 10 = 9 +  1 = 3**2 + 1**2 
# 8 = 4 + 4 = 2**2 + 2**2
def vrati_listu_kvadrata_sa_kojim_je_deljiv(broj):
    # 1 4 9 16 25 36 .... 
    kvadrati = []
    for i in range(1,broj):
        kvadrat = i**2
        # if kvadrat > broj:
            # break
        # if broj % kvadrat == 0:
        kvadrati.append(kvadrat)
    return kvadrati
def da_li_je_savrsen_kvadrat(broj):
    lista_kvadrata = vrati_listu_kvadrata_sa_kojim_je_deljiv(broj)
    print(lista_kvadrata)
    for element in lista_kvadrata:
        for drugi_element in lista_kvadrata:
            #print(element,drugi_element)
            print(element+drugi_element)
            if (element + drugi_element) == broj:
                print(element,"+",drugi_element)
                return True
    return False
    
    
# print(vrati_listu_kvadrata_sa_kojim_je_deljiv(36))
# print(da_li_je_savrsen_kvadrat(36))

# for i in range(1,1000):
    # if da_li_je_savrsen_kvadrat(i):
        # print(i)
    
print(da_li_je_savrsen_kvadrat(10))