l1 = [1,2,[3,4]]
l2 = l1 
# kada smo ovo uradili one postaju jedna te ista lista
l1.append(100)
l2.append(5)
print(l1,l2)
# ************************************
# shallow kopi kopira samo prvi "nivo", ne ide rekurzivno kroz elemente 
l1 = [1,2,[3,4]]
l2 = l1.copy()
l2[0] = 10
print(l1,l2)
l1[2][1] = 77 
print(l1,l2)
print("*"*100)
from copy import deepcopy # iz modula koji radi sa kopija uvozimo deepcopy funkciju
l1 = [1,2,[3,4]]
l2 = deepcopy(l1)
l2[0] = 10
print(l1,l2)
l1[2][1] = 77 
print(l1,l2)