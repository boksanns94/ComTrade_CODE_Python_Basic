# Fibonacijev niz pocinje sa dve jedinice 
# a svaki sledeci element je zbir prethodna dva 
# 1 1 2 3 5 8 13 21 34 55 89 144 ... 
     #n       n-2       n-1 
# fib(1) = 1
# fib(2) = 1 
# fib(3) = fib(1) + fib(2)
# fib(4) = fib(2) + fib(3)
# fib(5) = fib(3) + fib(4)
# fib(6) = fib(4) + fib(5)

def fib(n):
    print("Trenutno n",n)
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(5))
