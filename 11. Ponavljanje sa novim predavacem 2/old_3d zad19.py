import argparse
from os.path import isfile

def proveri_fajl(naziv_fajla):
    if not isfile(naziv_fajla):
        print(naziv_fajla,"ne postoji!")
        exit(1)
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--prvi",type=str,required=True,help="Prvi fajl")
    parser.add_argument("--drugi",type=str,required=True,help="Drugi fajl")

    args = parser.parse_args()
    proveri_fajl(args.prvi)
    proveri_fajl(args.drugi)
    with open(args.prvi,"r") as prvi_fajl:
        with open(args.drugi,"r") as drugi_fajl:

            brojac = 1
            redovi_prvog = prvi_fajl.readlines()
            redovi_drugog = drugi_fajl.readlines()
            for element_prvog,element_drugog in zip(redovi_prvog,redovi_drugog):
                if element_drugog != element_prvog:
                    print(brojac,end= " ")
                brojac+=1
            manji = min(len(redovi_drugog),len(redovi_prvog)) # 3
            veci = max(len(redovi_prvog),len(redovi_drugog)) # 7
            for i in range(veci-manji,veci+1):
                print(i,end=" ")

            




if __name__ == "__main__":
    main()