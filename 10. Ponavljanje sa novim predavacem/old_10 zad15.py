import argparse
from os.path import isfile
from sys import stderr

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--ulaz',type=str,required=True,help="Naziv ulaznog fajla")
    parser.add_argument('--k',type=int,required=True,help="Broj karaktera sa kojim poredimo")

    args = parser.parse_args()

    ime_ulaznog = args.ulaz
    k = args.k

    if not isfile(ime_ulaznog):
        print(ime_ulaznog,"ne postoji!",file=stderr)
        exit(1)
    
    with open(ime_ulaznog,"r") as fajl:

        redovi = fajl.readlines()
        print(redovi)
        for red in redovi:
            red = red.strip()
            if len(red) >= k:
                print(red)
if __name__ == "__main__":
    main()