limit = int(input("Введите колличество записей в список "))
l = []
element = 0
j = 0
while element < limit:
    l.append(input("Введите следующее значение списка "))
    element += 1
for i in range(int(len(l) / 2)):
    l[j], l[j + 1] = l[j + 1], l[j]
    j += 2
print(l)
