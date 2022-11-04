# funkcije koje pozivaju druge funkcije 
def foo():
    print("foo")
    bar()
    print("tek kad se zavrsi bar funkcija,nastavljamo dalje")

def bar():
    print("bar")
    #foo()
foo()