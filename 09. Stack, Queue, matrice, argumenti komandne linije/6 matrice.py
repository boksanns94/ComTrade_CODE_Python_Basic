
matrica = [
    # koji su potencijalni redovi u matrici? 
    [1,2,3], # 0 -> 0 1 2 
    [4,5,6], # 1 -> 0 1 2 
    [7,8,9], # 2 -> 0 1 2
    [1,2,3]  # 3 -> 0 1 2
    # 4 x 3 -> (00 do 32)
]

print(matrica)
print(matrica[1])
print(matrica[1][1])

broj_redova = len(matrica)
print(broj_redova,"reda")
broj_kolona = len(matrica[0])
print(broj_kolona,"kolone")
broj_kolona = len(matrica[-1])
print(broj_kolona,"kolone")

for i in range(broj_redova):
    # fiksiramo sa i trenutni red 
    # i=0
    for j in range(broj_kolona): # prodjemo kroz sve kolone  # sve vrednost od 0 do broj_kolona - 1
        print(matrica[i][j],end=" ")
        #print(f"{i}{j}",end=" ")

    print()

print()


for red in matrica:
    #print(red)
    for element in red:
        print(element,end=" ")
    print()

matrica =[[1,2,3]] * 5
print(matrica)
matrica[0][1] = 10
print(matrica)