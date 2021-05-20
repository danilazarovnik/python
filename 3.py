def my_func(x, y, z):
    if x >= z and y >= z:
        return x + y
    elif x > y and x < z:
        return x + z
    else:
        return y + z
a = int(input("набери первое число "))
b = int(input("набери второе число "))
c = int(input("набери третье число "))
print(my_func(a, b, c))
