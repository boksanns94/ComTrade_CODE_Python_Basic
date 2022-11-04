lista_neka = [1, 2, 3, 4, 5, 6]
print(lista_neka[0:3])
# istampace [1, 2, 3]

s = 'Python'
print(s[0:3])
# istampace 'Pyt'

s2 = 'Probna_rec'
slajs = slice(0, 3, 1)
print(s[slajs])
print(s[0:3:1])
# gornja dva printa ce da istampaju istu stvar



l = list(range(10))
print(l)
print(l[3:6])
l[3:6] = [100, 100, 100]
print(l)
del l[3:6]
print(l)