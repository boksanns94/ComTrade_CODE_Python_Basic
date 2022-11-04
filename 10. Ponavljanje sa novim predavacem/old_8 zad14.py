import argparse
from os.path import isfile
from sys import stderr
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ulaz',type=str,required=True,help="Naziv ulaznog fajla:")
    args = parser.parse_args()
    ime_fajla = args.ulaz
    # ime_fajla = "8_zad14.txt"
    if not isfile(ime_fajla):
        print("Los naziv fajla",file=stderr)
        exit(1)
    with open(ime_fajla,"r") as f:
        brojevi = f.read().split()
        print(brojevi)
        brojevi = [float(broj) for broj in brojevi]
        print(brojevi)

        trenutni_maks = brojevi[0]
        for broj in brojevi:
            if broj > trenutni_maks:
                trenutni_maks = broj
    print(trenutni_maks)


if __name__ == "__main__":
    main()