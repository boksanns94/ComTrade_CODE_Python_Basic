t = tuple([1,2,3])
print(t)

t = (1,2,3,4)
print(t[0])
#t[0] = 25

a=5
b=6
(a,b) = (b,a)
print(a,b)

def operacije(a,b):
    return a+b,a-b
print(operacije(5,6))

t2 =(10,20,30,[1,2,3])
print(t+t2)

print(t2[3])
t2[3][0] = 5
print(t2)

# EXOR
# 0 0    0   
# 0 1    1
# 1 0    1
# 1 1    0
skup1 = {1,2,3}
skup2 = {3,4,5}
print(skup1.intersection(skup2))
print(skup1[0])