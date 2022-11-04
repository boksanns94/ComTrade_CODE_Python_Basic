# operatori poredjenja u pajtonu

# >, >=, <, <= 
print("5>6",5>6)
print("5>3",5>3)
print("5<10",5<10)
print("10<=12",10<=12)

# == - operator poredjenja JEDNAKOSTI leve i desne strane.
# u slucaju da su vrednosti jednake -> True u suprotnom -> False
# != - operator za poredjenje NEJEDNAKOSTI leve i desne strane.
# ako su razlicita leva i desna strana -> True, ako nisu vraca False

# = - DODELA VREDNOSTI, RACUNA PRVO DESNU STRANU, PA UPISUJE U LEVU STRANU REZULTAT, on NIJE OPERATOR POREDJENJA!!!

print(5==5)
print(5==10)
print(10!=10.0)
print(55!=123)
print("asd" != 5 )
print()
print("CASTOVANJE U BOOL")
# castovanje u boolean ( logicki tip koji uzima samo True ili False)
print(bool(55))
print(bool(-55))
print(bool(-123.2))
print(bool("Zdravo"))
# jedine tri vrednosti koje daju netacan uslov konverzijom u bool
# su 0 "" i None

print(bool(0))
print(bool(""))
print(bool(None))
