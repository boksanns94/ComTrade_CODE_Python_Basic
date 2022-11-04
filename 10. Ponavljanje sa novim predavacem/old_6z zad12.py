

def main():
    izlaz = open("palindromi.txt","w")
    with open("datoteka.txt","r") as f:
        reci = f.read().split()
        for rec in reci:
            if rec == rec[::-1]:
                izlaz.write(rec + " ")
        
       # izlaz.write (" ".join([rec for rec in f.read().split() if rec == rec[::-1]]))
if __name__ == "__main__":
    main()