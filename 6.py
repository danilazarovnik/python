x = int(input("Введите количесто пройденых км в первый день "))
y = int(input("Введите желаемое количество км "))
day = 1
while y - x > 0:
    x = x + (x * 0.1)
    day += 1
print(day, "дней для достижения цели")
