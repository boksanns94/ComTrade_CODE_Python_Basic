def test(n):
    if n==0:
        return
    print("Cao")
    test(n-1)

test(5)
# napisati funkciju koja za argument prima neki broj i kao rezultat vraca njegov faktorijel
#                    n   n-1
# 5! = 5* 4*3*2*1  = 5 * 4! = 5 * 24 = 120
# 4! = 4* 3*2*1 =    4 * 3! = 4 * 6 = 24
# 3! = 3* 2*1   =    3 * 2! = 3 * 2 = 6
# 2! = 2 * 1    =    2 * 1! = 2 * 1 = 2 
# 1! = 1
# ako je n == 1 -> 1
# ako je bilo koji drugi broj sta vracamo -> 
def faktorijel(n):
    if n==1:
        return 1
    
    return n * faktorijel(n-1)
print(faktorijel(5))