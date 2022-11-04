        
n=10
for i in range(n): # i ce uzimati sve vrednosti od 0 do 2 
    for j in range(n): # i za svako i, j ce uzimati vrednosti od 0 do 2
        #print(f"{i}{j}",end=" ")
        if i==j or i+j == n-1 or i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    #print()
        
        
# *******
# **   **
# * * * *
# *  *  *
# * * * *
# **   **
# *******

# napraviti sahovksku tablu
# * * * * 
#  * * * *
# * * * * 
#  * * * *
# * * * * 
#  * * * *
# * * * * 
#  * * * *
      