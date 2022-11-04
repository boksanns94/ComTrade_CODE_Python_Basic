import argparse
from os.path import isfile
from sys import stderr
def parsiraj_ulazne_argumente():
    """

    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--ulaz',type=str,required=True,help="Naziv ulaznog fajla")
    parser.add_argument('--k',type=int,required=True,help="Broj karaktera sa kojim poredimo")

    args = parser.parse_args()
    return args
def proveri_da_li_je_fajl_dobar(ime_ulaznog):
    if not isfile(ime_ulaznog):
        print(ime_ulaznog,"ne postoji!",file=stderr)
        exit(1)
    return ime_ulaznog
def ispisi_duze_od_n_karaktera(lista_stringova,minimalna_duzina):
    for red in lista_stringova:
        red = red.strip()
        if len(red) >= minimalna_duzina:
            print(red)
def main():
    
    args = parsiraj_ulazne_argumente()
    ime_ulaznog = args.ulaz
    k = args.k
    ime_ulaznog = proveri_da_li_je_fajl_dobar(ime_ulaznog)
    
    
    with open(ime_ulaznog,"r") as fajl:

        # redovi = fajl.readlines()
        # print(redovi)
        ispisi_duze_od_n_karaktera(fajl.readlines(),k)
        
if __name__ == "__main__":
    main()