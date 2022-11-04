# napraviti sledeci sablon za dimenziju n 
# n = 5
# *****
# *   *
# *   *
# *   *
# *****

# n=2 
# **
# **

# n = 7 
# *******
# *     * -> zvezdica na pocetku i zvezdicu na kraju, sta je izmedju? 
# *     * -> z:1 r: z:1    z+z + r = n -> r = n - 2 
# *     *
# *     *
# *     *
# *******
# prvi i poslednji red imaju po n zvezdica
# kako izgledaju ostali redovi?

n = int(input("Unesite dimenziju sablona:"))
for i in range(n): # i uzima vrednosti : od 0 do n-1 
    if i == 0 or i == n-1:
        print(n * "*")
    else:
        #print("*" + (n-2) * " " + "*")
        print(f"*{(n-2) * ' '}*")
    