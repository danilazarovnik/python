def my_func(x, y):
    #return 1 / x ** abs(y)
    #return pow(x, y)
    z = 1
    y = abs(y)
    while (y > 0):
        z *= x
        y -= 1
    return 1 / z
print(my_func(2, -3))
