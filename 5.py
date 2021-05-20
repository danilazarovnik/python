revenue = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if revenue > costs:
    profit = revenue - costs
    profitability = profit / revenue
    print("Фирма работает с прибылью. Рентабельность выручки составила ", profitability)
else:
    print("Фирма работает в убыток или на ноль")
workers = int(input("Введите количество сотрудников фирмы "))
profitone = profit / workers
print("Прибыль в расчете на одного сторудника ", profitone)
