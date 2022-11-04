# Napisati rekurzivnu funkciju napravi_niz(broj) koja kreira niz 
# cifara datog celog  broja. Napisati rekurzivnu funkciju 
# ispisi_niz(niz, index) koja ispisuje elemente niza dužine n.

def napravi_niz_rekurzivno(broj):
    if broj == 0:
        return []
    return napravi_niz_rekurzivno(broj//10) + [broj%10]

def ispisi_niz_rekurzivno(niz):
    if len(niz) == 0:
        return
    print(niz[0], end=" ")
    ispisi_niz_rekurzivno(niz[1::])



# Main

n = int(input("Unesite broj: "))
print(f"Lista od broja {n} je {napravi_niz_rekurzivno(n)}.")
print(f"Ispisana lista rekurzivno: ", end="")
ispisi_niz_rekurzivno(napravi_niz_rekurzivno(n))