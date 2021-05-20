goods = []
while input("Если хотите добавить товар напишите 'да' ") == 'да':
    number = int(input("Напишите номер товара "))
    features = {}
    while input("Если хотите добавить параметр товара напишите 'да' ") == 'да':
        feature_key = input("Введите характеристку товара ")
        feature_value = input("Введите значение характеристики товара ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)

analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
            analitics[feature_key] = [feature_value]
print(analitics)
