from itertools import count
from itertools import cycle

for el in count(3):
    if el > 10:
        break
    print(el)

a = 0
my_list = ['ABC', 123, True]
for el in cycle(my_list):
    if a > 11:
        break
    print(el)
    a += 1
