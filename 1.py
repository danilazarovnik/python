def my_func(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y не должен быть нулем"
print(my_func(int(input("набери число x = ")), int(input("набери число y = "))))
