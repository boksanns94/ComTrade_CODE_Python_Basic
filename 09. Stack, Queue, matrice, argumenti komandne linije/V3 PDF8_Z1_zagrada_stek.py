# Unosi se aritmeticki izraz kao string, npr: 2+3*(5-2)
# Napisati program koji proverava da li su zagrade pravilno uparene.
# Uraditi sa stekom

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

def zagrade_sa_stekom(stek, izraz):
    for znak in izraz:
        if znak == "(":
            push(stek, znak)
        elif znak == ")":
            if pop(stek) == None:
                return False
    if len(stek) != 0:
        return False
    return True

stek = []

test_pravilan = "(2+3)* ( 5 - 2 ) "
test_puno_otvorenih = "(2+3)* ( 5 - 2 )( "
test_puno_zatvorenih = "(2+3)* )( 5 - 2 ) "
print(zagrade_sa_stekom(stek, test_pravilan))
print(zagrade_sa_stekom(stek, test_puno_zatvorenih))
print(zagrade_sa_stekom(stek, test_puno_otvorenih))