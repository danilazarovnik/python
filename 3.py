with open('tri_zp.txt', 'r') as my_file:
    familiya = []
    oklad = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           oklad.append(i[0])
        familiya.append(i[1])
print('Оклад меньше 20.000', oklad, 'средний оклад:', sum(map(int, familiya)) / len(familiya))
