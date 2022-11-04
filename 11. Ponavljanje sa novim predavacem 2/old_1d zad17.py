import argparse
from os.path import isfile
def prebroj_ponavljanja_podstringa(tekst,potencialni_podstring):
    # lampa stolica stopa
    # trazimo rec sto
    brojac = 0 # brojac je 0 zato sto brojimo koliko ih ima
    duzina_podstringa = len(potencialni_podstring)
    for i in range(len(tekst)-duzina_podstringa):
       # print(tekst[i:i+duzina_podstringa])
        if tekst[i:i+duzina_podstringa] == potencialni_podstring:
            brojac+=1
    return brojac    


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--ulaz",type=str,required=True,help="Naziv ulaznog fajla")
    # ,nargs="+" omogucava da imamo vise argumenata za isti ulazni podatak. i oni se posmatraju kao lista

    parser.add_argument("--rec",type=str,required=True,help="Rec koju trazimo")
    parser.add_argument("--izlaz",type=str,required=True,help="Naziv izlaznog fajla")

    args = parser.parse_args()
    #print(args.rec)

    n = int(input("Unesite trazeni minimalni broj ponavljanjaa za neku rec:"))

    if not isfile(args.ulaz):
        print("Ulazni fajl ne postoji!")
        exit(1)
    
    with open(args.ulaz,"r") as ulazni_fajl:
        with open(args.izlaz,"w") as izlazni_fajl:
            # redovi_ulaznog_fajla = ulazni_fajl.readlines()
            
            # for i in range(len(redovi_ulaznog_fajla)):
            #     if prebroj_ponavljanja_podstringa(redovi_ulaznog_fajla[i],args.rec) >= n:
            #         izlazni_fajl.write(f"{i}:{redovi_ulaznog_fajla[i]}")

            ulazni_fajl.seek(0)
            brojac = 0
            while True:
                red = ulazni_fajl.readline()
                if not red:
                    break 
                if prebroj_ponavljanja_podstringa(red,args.rec) >= n:
                    izlazni_fajl.write(f"{brojac}:{red}")
                brojac+=1



if __name__ == "__main__":
    main()
    #print(prebroj_ponavljanja_podstringa("stolicastopica","sto"))