def obrni_listu(brojevi):
    if len(brojevi) == 0:
        return []
    poslednji_element_liste = brojevi[-1]
    return [poslednji_element_liste] + obrni_listu(brojevi[:-1])
brojevi = [1,2,3,4]
print(obrni_listu(brojevi))
# [1,2,3,4] -> [4] + rek([1,2,3]) =[4] + [3,2,1] = [4,3,2,1]
# rek[1,2,3] = [3] + rek([1,2]) = [3] + [2,1] = [3,2,1]
# rek[1,2] = [2] + rek([1]) [2] + [1] = [2,1]
# rek[1] = [1] + rek([]) = [1] + [] = [1]
# rek([]) = []