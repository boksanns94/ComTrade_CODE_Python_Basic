# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:18:26 2021

@author: Boksan
"""

a = 2
b = 6.9
c = 420.420
# istampati a + b + c = rezultat
print(a, "+", b, "+", c, "=", a+b+c)
#printom je tesko stampati

#funkcija format je bolja
print("{} + {} + {} = {}:".format(a,b,c,a+b+c))
print("{3} + {2} + {1} = {0}:".format(a,b,c,a+b+c))
print("{:<10.2f} tekst".format(c))

#f stringovi
print(f"{a} + {b} + {c:<10.2f} = {a+b+c}")