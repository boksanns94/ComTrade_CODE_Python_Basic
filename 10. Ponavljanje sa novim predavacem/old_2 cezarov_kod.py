
def cezarov_shift(karakter:str,broj_mesta:int,smer:str) -> str:
    # abc,3,l -> xyz

    if smer.lower() == 'l':
        novi_znak = ord(karakter) - broj_mesta
        if novi_znak < ord("a"):
            # 'a' 3 l -> 92 - 3 = 89 
            # 89 je manje od 92 -> 119 - 2 = 117 ( x )
            prekoracenje = ord('a') - novi_znak # 92 - 89 = 3 
            novi_znak = chr(ord("z") - prekoracenje + 1)
            return novi_znak
        else:
            return chr(novi_znak)
    if smer.lower() == 'd':
        novi_znak = ord(karakter) + broj_mesta
        if novi_znak > ord('z'):
            prekoracenje = novi_znak - ord('z') 
            novi_znak = chr(ord('a') + prekoracenje - 1 )
            return novi_znak
        else:
            return chr(novi_znak)
def main():
    for slovo in "abcdxyz":

        print(cezarov_shift(slovo,3,"l"))

    for slovo in "xyz":

        print(cezarov_shift(slovo,3,"d"))

if __name__ == "__main__":
    main()

brojevi = [1,2,3,4]
brojevi.sort() 

sorted(brojevi)

# a=5
# a.sort()
tekst = 'a\tb\n cewr \tqwe'
print(tekst.split())