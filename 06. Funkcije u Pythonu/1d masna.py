#masna
#*    *   i:0 z:1 r:4 z:1
#**  **   i:1 z:2 r:2 z:2
#******   i:3 z:3 r:0 z:3
#**  **   i:1 z:2 r:2 z:2
#*    *   i:2 z:1 r:4 z:1
# i + z = const (n) 
# z = n-i
# 2 * z + r = 2 *n
# r = 2*n - 2 * z = 2*n - 2 *(n-i) = 2*n - 2*n + 2*i = 2*i 


#2*z + r = 2*n
# z = i + 1
# r = 2*n - 2 * z = 2 * n - 2 *(i+1) = 2*n - 2*i - 2 

#n=3
n=int(input("Unesite dimenziju sablona:"))
for i in range(n):
    print("*" * (i+1) + " " * (2*n - 2*i - 2 ) + "*" * (i+1))
for i in range(1,n):
    print("*" * (n-i) + " " * (2*i) + "*" * (n-i) )
    
