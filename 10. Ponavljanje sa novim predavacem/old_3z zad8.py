from sys import argv

from os.path import isfile
def main():
    if len(argv) !=2:
        print("Los broj argumenata")
        exit(1)
    
    ime_fajla = argv[1]
    if not isfile(ime_fajla):
        print(ime_fajla,"ne postoji")
        exit(1)
    fajl = open(ime_fajla,"r")
    stek = []
    otvorene = ["(","[","{"]
    zatvorene = [')',']','}']
    while True:
        karakter = fajl.read(1)
        if not karakter:
            break
        if karakter in otvorene:
            stek.append(karakter)
            #print(stek)
        elif karakter in zatvorene:
            if len(stek) == 0:
                print("Lose su uparene zagrade,ima vise ) u nekom trenutku")
                exit(1)
            else:
                
                pozicija_u_listi_zagrada = zatvorene.index(karakter)
                #print(pozicija_u_listi_zagrada)
                odgovarajuca_zagrada_otvorena = otvorene[pozicija_u_listi_zagrada]
                if stek[-1] == odgovarajuca_zagrada_otvorena:
                    stek.pop()
                else:
                    print("Lose uparene zagrade")
                    exit(1)

    if len(stek) == 0:
        print("Dobre zagrade")
    else:
        print("Ima vise otvorenih nego zatvorenih zagrada!")
if __name__ == "__main__":
    main()