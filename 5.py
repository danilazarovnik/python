number = int(input("Введите число "))
my_list = [7, 4, 3, 3, 2]
poisk = my_list.count(number)
for element in my_list:
    if poisk > 0:
        i = my_list.index(number)
        my_list.insert(i+poisk, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)
