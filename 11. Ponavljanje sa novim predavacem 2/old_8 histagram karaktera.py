# danas 
# d = > 1
# a = > 2
# n => 1
# s => 1
# 1/5 2/5 1/5 1/5 -> 20% 20% 40% 20% 
# round(VREDNOST / ukupno) * 100
# d: ********************
# n: ********************
# s: ********************
# a: ****************************************

# Koristeci argumente komande linije ucitati naziv fajla koji nam je izvor za tekst.
# 1)a zatim prebrojati koji karakter se koliko puta ponavlja
# 2)pronaci karakter koji se najcesce ponavlja
# 3) nacrtati histagram sa * u formi nacrtanoj kao sto je gore
def napravi_recnik_ponavljanja(tekst):
    recnik = {}
    for karakter in tekst:
        if karakter not in recnik.keys():
            recnik[karakter] = 1
        else:
            recnik[karakter] +=1
        #print(recnik)
    return recnik
def najcesci_karakter(recnik_ponavljanja):
    najvise_ponavljanja = max(recnik_ponavljanja.values())
    karakteri_sa_najvise = [karakter for karakter in recnik_ponavljanja.keys() if recnik_ponavljanja[karakter] == najvise_ponavljanja]
    if len(karakteri_sa_najvise) == 1:
        return karakteri_sa_najvise[0]
    else:
        return karakteri_sa_najvise
def histagram(recnik_ponavljanja):
    ukupno_karakter = sum(recnik_ponavljanja.values())
    for karakter in recnik_ponavljanja.keys():
        procenat = round(recnik_ponavljanja[karakter]* 100 / ukupno_karakter) 
        print(f"{karakter}:{procenat * '*'}")
import argparse
from os.path import isfile
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--ulaz",type=str,required=True,help="Naziv ulaznog fajla:")

    args = parser.parse_args()

    if not isfile(args.ulaz):
        print("Ne postoji fajl sa tim imenom.")
        exit(1)
    with open(args.ulaz,"r") as f:
        recnik_ponavljanja = napravi_recnik_ponavljanja(f.read())
        print(recnik_ponavljanja)
        print(najcesci_karakter(recnik_ponavljanja))
        histagram(recnik_ponavljanja)
    
if __name__ == "__main__":
    main()
