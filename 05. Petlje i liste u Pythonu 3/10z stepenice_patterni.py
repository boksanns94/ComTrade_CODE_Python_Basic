# Sabloni sa "stepenicama"
# korisnik unosi n zatim treba ispisati odgovarajuci sablon dimenzije n uz pomoc *
# n=3 
# *
# **
# ***

# n=5      i      i+1
# *      i:0 -> z:1
# **     i:1 -> z:2
# ***    i:2 -> z:3
# ****   i:3 -> z:4
# *****  i:4 -> z:5
# 
n = int(input("Unesite dimenziju sablona:"))
for i in range(n): # i ce uzimati vrednosti od 0 do n-1 ( npr ako je n=5 od 0 do 4)
    print((i+1) * "*")

# 2. 
# n=3 
#   *
#  **
# ***

# n=5
#     * i:0 r:4 z:1
#    ** i:1 r:3 z:2
#   *** i:2 r:2 z:3
#  **** i:3 r:1 z:4
# ***** i:4 r:0 z:5


# broj_zvezdica = i + 1 
# koliko ce biti razmaka?
# broj_zvezdica + broj_razmaka = n 
# broj_razmaka = n - broj_zvezdica = n - (i+1) = n-i-1

print()
for i in range(n):
    print(" " * (n-i-1) + "*" * ( i + 1 ))
# for i in range(n): # i ce uzimati vrednosti od 0 do n-1 ( npr ako je n=5 od 0 do 4)
    # print(f"{(i+1) * '*':>{n}}")
    
# 3. n=5
# ***** i:0 r:0 z:5 
#  **** i:1 r:1 z:4 
#   *** i:2 r:2 z:3 
#    ** i:3 r:3 z:2 
#     * i:4 r:4 z:1 
# r -> i
# z + r = n
# z = n - r = n- i

# 4. n=5
# *****
# ****
# ***
# **
# *

# 5. n = 5
#     *
#    ***
#   *****
#  *******
# *********
#    |||


# 6. n=5
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# n=5
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *





