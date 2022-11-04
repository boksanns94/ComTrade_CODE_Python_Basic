# Napisati funkciju koja prima n, koja vraca nti element niza. 
# Niz je 1 5 10 14 19 23 28 32… Prvi elementi niza su uvek 1, 5 i 10. 
# Svaki sledeci je 5+10-1 (=14). Uraditi iterativno i rekurzivno.

# Iterativno
def iterativno_nti_element(n):
    if n == 1:
        return 1
    if n == 2:
        return 5
    if n == 3:
        return 10
    if n > 3:
        prvi = 1
        drugi = 5
        treci = 10
        for i in range(4,n+1):
            nti = drugi+treci-prvi
            prvi = drugi
            drugi = treci
            treci = nti
        return nti

# Rekurzivno

def rekurzivno_nti_element(n):
    if n == 1:
        return 1
    elif n == 2:
        return 5
    elif n == 3:
        return 10
    else:
        return rekurzivno_nti_element(n-2)+rekurzivno_nti_element(n-1)-rekurzivno_nti_element(n-3)



# Main

print(iterativno_nti_element(7))
print(rekurzivno_nti_element(7))