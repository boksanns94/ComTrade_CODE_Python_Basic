# napisati funkciju koja prima broj i vraca njegov faktorijel

# 5! = 5* 4*3*2*1 = 5 * 4!
# 4! = 4* 3*2*1   = 4 * 3!
# 3! = 3* 2*1     = 3 * 2!
# 2! = 2* 1       = 2 * 1!
# 1! = 1

def faktorijel(n):
    print(n, "pokretanje")
    if n == 1:
        return n
    return n*faktorijel(n-1)

print(faktorijel(5))

# napisati funkciju koja prima broj i racuna vrednost elemnta fibonacijevog niza

# fib(6) = fib(5) + fib(4)
# fib(5) = fib(4) + fib(3)
# fib(4) = fib(3) + fib(2)
# fib(3) = fib(2) + fib(1)
# fib(2) = 1
# fib(1) = 1

def fibonaci(n):
    print(n, "pokretanje")
    if n == 1 or n == 2:
        return 1
    return fibonaci(n-1)+fibonaci(n-2)

print(fibonaci(10))