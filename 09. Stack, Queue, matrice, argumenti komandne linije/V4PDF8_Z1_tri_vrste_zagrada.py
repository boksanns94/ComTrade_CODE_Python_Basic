# resiti zadatak ali proveravati da vrste zagrada () [] {}

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

def zagrade_konacno(izraz):
    for znak in izraz:
        if znak in lista_otvorenih:
            push(stek, znak)
        elif znak in lista_zatvorenih:
            zagrada = pop(stek)
            if zagrada == None:
                return False
            if lista_otvorenih.index(zagrada) != lista_zatvorenih.index(znak):
                return False
    if len(stek) == 0:
        return True
    return False

lista_otvorenih = ["(", "[", "{"]
lista_zatvorenih = [")", "]", "}"]
stek = []

test_pravilan = "({[]})"
test_nepravilan1 = "({[)})"
test_nepravilan2 = "{{[()]]]"
print(zagrade_konacno(test_pravilan))
print(zagrade_konacno(test_nepravilan1))
print(zagrade_konacno(test_nepravilan2))