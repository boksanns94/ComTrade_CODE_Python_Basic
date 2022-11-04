
from os.path import isfile


def main():
    
    
    izlaz = open("1d1_rotacije.txt","w")
    unos = input("Unesite tekst:")
    n = len(unos)
    for i in range(n):
        izlaz.write(unos[n-i:] + unos[:n-i] + "\n")
    izlaz.close()

if __name__ == "__main__":
    main()