# Napisati funkcije push i pop, simulirati stack.
# Maksimalan broj elemenata je 10.
# Implementirati preko jedne obicne liste.

def push(lista, element):
    if len(lista) < 10:
        lista.append(element)
        return True
    print("Ne mozemo da dodamo element na stack, stack je pun! STACKOVERFLOW")
    return False

def pop(lista):
    if len(lista) == 0:
        print("Ne mozemo da izbacimo element sa praznog stacka! STACKUNDERFLOW")
        return False
    poslednji = lista.pop()
    return poslednji

stek = []
push(stek, 10)
push(stek, 15)
push(stek, 11)
print(stek)
for i in range(len(stek)):
    pop(stek)
print(stek)