# Napisati rekurzivnu funkciju koja pronalazi najmanji element u listi

def najmanji_element_rekurzivno(lista_brojeva):
    if len(lista_brojeva) == 1:
        return lista_brojeva[0]
    if lista_brojeva[0] < najmanji_element_rekurzivno(lista_brojeva[1::]):
        return lista_brojeva[0]
    return najmanji_element_rekurzivno(lista_brojeva[1::])



# Main

lista_brojeva = [6,7,3,8,1,9,-1,10,5,4]
print(f"Najmanji element u listi {lista_brojeva} je: {najmanji_element_rekurzivno(lista_brojeva)}.")