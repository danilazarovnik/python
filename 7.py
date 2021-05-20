from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)

a = fact()
b = 0
for i in a:
    if b < 15:
        print(i)
        b += 1
    else:
        break
