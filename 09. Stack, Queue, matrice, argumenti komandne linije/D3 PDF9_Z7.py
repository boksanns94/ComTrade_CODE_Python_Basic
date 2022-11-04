# PDF9 - Zadatak 7
#
# Kao argument komandne linije učitava se string koji predstavlja apsolutnu
# Unix-like putanju. Napisati program koji vraća koja je to putanja nakon što ju je
# pojednostavio.
# Napomena: Apsolutna putanja uvek počinje sa /, putanja u sebi ne sadrži beline

from sys import argv

if len(argv) != 2:
    print("Pogresan unos argumenata. Unesite ime fajla i putanju.")
    exit()

putanja = argv[1].split("/")
if putanja[-1] == "":   # ako je na kraju ostala kosa crta bice prazan element viska
    putanja.pop()

pojednostavljena_putanja = []
for i in range(len(putanja)):
    level = putanja[i]
    pojednostavljena_putanja.append(level)
    if level == ".":
        pojednostavljena_putanja.pop()
    elif level == "..":
        pojednostavljena_putanja.pop()
        pojednostavljena_putanja.pop()

konacna_putanja = "/".join(pojednostavljena_putanja)
print(f"Pojednostavljena putanja je {konacna_putanja}.")