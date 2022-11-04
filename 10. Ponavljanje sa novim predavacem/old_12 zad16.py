import argparse
from os.path import isfile
from sys import stderr

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--ulaz',type=str,required=True,help="Naziv ulaznog fajla")
    

    args = parser.parse_args()

    ime_ulaznog = args.ulaz

    if not isfile(ime_ulaznog):
        print(ime_ulaznog,"ne postoji!",file=stderr)
        exit(1)
    
    with open(ime_ulaznog,"r") as fajl:

        redovi = fajl.readlines()
        #print(redovi)
        trenutni_maks = len(redovi[0].strip())
        lista_najduzih_redova = [redovi[0].strip()]
        for red in redovi[1:]:
            red = red.strip()
            if len(red) > trenutni_maks:
                lista_najduzih_redova =[red]
            if len(red) == trenutni_maks:
                lista_najduzih_redova.append(red)
        print(lista_najduzih_redova)
    lista_najduzih_redova.sort()
    print(lista_najduzih_redova[0])
if __name__ == "__main__":
    main()