import json
profit = {}
sredn_profit = {}
x = []
prof = 0
sredn_individ_profit = 0
i = 0
with open('seven.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    x.append(profit)
    print(x)
    if i != 0:
        sredn_individ_profit = prof / i
        print('Прибыль средняя - ', sredn_individ_profit)
    else:
        print('Прибыли нет. Все работают в убыток')
    sredn_profit = {'srednyaya pribl': round(sredn_individ_profit)}
    profit.update(sredn_profit)
    print('Прибыль каждой компании - ', x)
with open('seven_j.json', 'w') as write_js:
    json.dump(x, write_js)
    js = json.dumps(x)
    print('Файл с расширением json: \n', js)
