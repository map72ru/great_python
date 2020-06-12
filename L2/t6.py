goods = []

n = 1
while True:

    name = input('Введите название товара (пусто выход): ')
    if name == '':
        break

    price = input('Введите цену товара: ')
    while not price.replace('.', '', 1).isdigit():
        price = input('Не верно. Введите еще раз: ')
    price = float(price)

    weight = input('Введите вес товара в кг.: ')
    while not weight.replace('.', '', 1).isdigit():
        weight = input('Не верно. Введите еще раз: ')
    weight = float(weight)

    qnt = input('Введите количество товара в шт.: ')
    while not qnt.isdigit():
        qnt = input('Не верно. Введите еще раз: ')
    qnt = int(qnt)
    # собираем структуру
    goods.append((n, {'Название': name, 'Цена': price, 'Вес': weight, 'Количество': qnt}))


# Анализ товаров
analyze = {}

for good in goods:
    for item in good[1].items():
        if analyze.get(item[0]) is None:
            analyze.update({item[0]: {item[1]}})
        else:
            s = analyze.get(item[0])
            s.add(item[1])

print('Анализ: ', analyze)