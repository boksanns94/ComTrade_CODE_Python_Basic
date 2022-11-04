brojevi = [3,4,1,2,3,222,123,22]

parni = [] 
for broj in brojevi:
    if broj % 2==0:
        parni.append(broj)
print(parni)

p = [broj*5 for broj in brojevi if broj % 2==0]
print(p)

tekst = "anavolimilovana"
if tekst == tekst[::-1]:
    print(tekst,"je palindrom")
else:
    print(tekst,"nije palindrom")

# kako bismo ovo uradili sa pretpostavkom
pretpostavka = True 
# 01234
# kapak
# n=5
#  i     n-1-i
# [0] = [4]
# [1] = [3]
# [2] = [2]
# [3] = [1]
# [4] = [0]
n=len(tekst)
for i in range(n):
    if tekst[i] != tekst[n-1-i]:
        pretpostavka=False
        break
if pretpostavka:
    print("Jeste palindrom")
else:
    print("Nije palindrom")


