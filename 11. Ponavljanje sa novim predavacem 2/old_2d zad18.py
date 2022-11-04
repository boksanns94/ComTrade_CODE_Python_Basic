def main():
    kraj_linije = input("Unesite ekstenziju za pretragu.")
    brojac =0
    with open("ulaz.txt","r") as fajl:
        while True:
            red = fajl.readline()
            if not red:
                break
            #print(red.strip())
            if red.strip().endswith(kraj_linije):
                brojac+=1
    print(brojac)
if __name__ == "__main__":
    main()
        
