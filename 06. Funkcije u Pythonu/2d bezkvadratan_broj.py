# bezkvadratan broj
# broj je bezkvadratan ako nije deljiv ni sa jednim kvadratom nekog broja 
# 42 => 1 2 3 6 7 14 21 42 je bezkvadratan jer nijedan od delilaca osim 1 nije kvadrat nekog broja 
# 45 => je deljiv sa 9 -> on nije bezkvadratan
n = int(input("Unesite neki broj za proveru da li je bezkvadratan:"))
pretpostavka = True
for i in range(2,n):
    # treba da proverimo da li je deljiv sa 4,9,16,25,36,49,64....
    # 4 = 2**2 
    # 9 = 3**2 
    # 16 = 4**2 
    #print(i**2)
    if n % i ** 2 == 0:
        pretpostavka = False
        break
if pretpostavka:
    print(n,"je bezkvadratan")
else:
    print(n,"nije bezkvadratan")
    

