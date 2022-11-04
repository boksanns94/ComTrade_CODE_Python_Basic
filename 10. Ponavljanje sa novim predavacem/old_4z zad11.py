from sys import argv
from os.path import isfile
import argparse
def main():
    if len(argv) !=2 :
        print("Los unos argumenata, potrebno je tacno 2!")
        exit(1)
    if not isfile(argv[1]):
        print("Fajl ne postoji!")
        exit(1)
    
    with open(argv[1],"r") as f:
       
        reci = [rec for rec in f.read().split()]
        print(len(reci))
if __name__ == "__main__":
    main()