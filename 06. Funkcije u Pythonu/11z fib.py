# fibonacijev niz je niz koji pocinje sa dve jedinice,a svaki sledeci element je jednak zbiru 
# dva prethodna.
#1 1 2 3 5 8 13 21 34 55 89 ...
# funkcija koji prima kao argument n i vraca n-ti element fibonacijevog niza
def fib(n):
    prethodni_element = 1
    jos_jedan_iza = 1 
    sledeci_element = 1
    for i in range(n-2):
        sledeci_element = prethodni_element + jos_jedan_iza # 2  3   5  8
        jos_jedan_iza = prethodni_element # 1  2 3 5 
        prethodni_element = sledeci_element # 2 3  5  8
    return sledeci_element
    
def fib_py(n):
    prethodni_element,jos_jedan_iza = 1 ,1
    for i in range(n-2):
        prethodni_element,jos_jedan_iza = prethodni_element + jos_jedan_iza, prethodni_element
    return prethodni_element
        
    
    
print(fib(6)) # -> 8
print(fib(1))
print(fib_py(10))

for i in range(1,21):
    print(fib(i),end=" ")
# kako biste ispisali sve elemente fib niza koji su manji od milion?
trenutna_pozicija_fib = 1
print()
while fib(trenutna_pozicija_fib) < 1000000:
    print(fib(trenutna_pozicija_fib),end=" ")
    trenutna_pozicija_fib +=1
    
    