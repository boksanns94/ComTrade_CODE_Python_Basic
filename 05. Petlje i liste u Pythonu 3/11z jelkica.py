# jelkica
# 5. n = 5    i  
#     *     i:0 r:4 z:1 r:4
#    ***    i:1 r:3 z:3 r:3
#   *****   i:2 r:2 z:5 r:2
#  *******  i:3 r:1 z:7 r:1
# ********* i:4 r:0 z:9 r:0


# i + r = 4 ( n - 1 )
# r = n-1-i 

# ukupno mesta u redu ima 2 * n - 1 
# n=5 -> ima 9 mesta 5*2 - 1 = 9
# n=7 -> ima 13 mesta -> 7 * 2 - 1 = 13
# r + z + r = 2*n -1 
# r = n-1-i
# z + 2r = 2*n-1
# z + 2*(n-1-i) = 2*n - 1
# z + 2*n - 2 - 2*i = 2*n -1 
# z = 2*n - 1 - 2*n +2 +2i
# z = 2*i + 1
n = int(input("Unesite dimenziju sablona:"))
for i in range(n):
    print(" " * (n-1-i) + "*" * (2*i + 1))
    
#  ****
# *
# *
# *
#  ****
print()
brojac_zvezdica = 1 # on vodi racuna koliko zvezdica imate trenutno u redu
for i in range(n):
    print(" " * (n-1-i) + brojac_zvezdica * "*")
    brojac_zvezdica = brojac_zvezdica + 2
    
# 6. n=5
#     *
#    ***
#   *****
#  *******
# *********
# ********* i:0 r:0 z:9 r:0
#  *******  i:1 r:1 z:7 r:1
#   *****   i:2 r:2 z:5 r:2
#    ***    i:3 r:3 z:3 r:3
#     *     i:4 r:4 z:1 r:4

# razmaci = i
# 2* razmaci + zvezdice = 2*n- 1
# zvezdice = 2*n - 1 - 2*i

for i in range(n):
   brojac_zvezdica = brojac_zvezdica - 2 
   print(" " * i + brojac_zvezdica * "*") 
print()
for i in range(n):
    print(" " * (n-1-i) + "*" * (2*i + 1))
for i in range(n):
    print(" " * i + "*" * (2*n -1 -2*i))
print()
brojac_zvezdica = 1 
for i in range(2*n):
    if i < n:
        print(" " * (n-1-i) + brojac_zvezdica * "*")
        brojac_zvezdica = brojac_zvezdica + 2
    else:
        brojac_zvezdica = brojac_zvezdica - 2 
        print(" " * (i-n) + brojac_zvezdica * "*") 









