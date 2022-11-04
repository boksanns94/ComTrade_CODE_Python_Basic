
broj = int(input("Unesite neki broj:"))
for i in range(2,broj//2+1):
    if broj % i == 0:
        print("Nije prost")
        break
else: # else deo se desava samo ako se nijednom nije desio break u petlji
    print("Prost je broj")

brojevi = [1,2,3,4]
#parni = [sta_ubacujemo prolazak_kroz_petlju [OPCIONO USLOV]]
parni = [broj for broj in brojevi if broj % 2 == 0]
print(parni)

print(type(parni))
print(type(print))
# a=123
# a.sort()
# sorted()