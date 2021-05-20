second = int(input("Введите секнды "))
h = ((second//3600) % 24)
m = ((second // 60) % 60)
s = (second % 60)
if m < 10:
    m = str('0' + str(m))
else:
    m = str(m)
if s < 10:
    s = str('0' + str(s))
else:
    s = str(s)
print(str(h) + ':' + m + ':' + s)
