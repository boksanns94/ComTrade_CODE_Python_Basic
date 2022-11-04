import argparse
from os.path import isfile
def prebroj_cifre(broj):
    broj = abs(broj)

    brojac = 0
    while (broj > 0):
        brojac+=1
        broj //=10
    return brojac
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--ulaz",type=str,required=True,help="Naziv ulaznog fajla")
    parser.add_argument('--k',type=int,required=True,help="Koliko cifara ima taj broj")

    args = parser.parse_args()
    print(args)

    if not isfile(args.ulaz):
        print(f"Greska,los naziv fajla!{args.ulaz} ne postoji")
        exit(1)
    with open(args.ulaz,"r") as fajl:
        ukupno_brojeva = int(fajl.readline().strip())
        red = fajl.readline()
        print(red)
        delovi_reda = red.split()
        print(delovi_reda)
        brojevi = [int(broj) for broj in delovi_reda]
        print(brojevi)
        #koliko_cifara = [broj for broj in brojevi if prebroj_cifre(broj) == args.k]
        brojac = 0
        for broj in brojevi:
            print(f"{broj} ima {prebroj_cifre(broj)} cifara")
            if prebroj_cifre(broj) == args.k:
                brojac+=1
    print(f"Ima ukupno {brojac} {args.k}-tocifrenih brojeva")

if __name__ == "__main__":
    main()