stroka = input("Введите строку ")
a = stroka.split()
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(i, '-', el)
