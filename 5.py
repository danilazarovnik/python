def my_sum():
    sum_res = 0
    vihod = False
    while vihod == False:
        number = input("Набери числа через пробел или Q для выхода: ").split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                vihod = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print("Сумма введенных чисел ", sum_res)
    print("Общая сумма ", sum_res)
my_sum()
