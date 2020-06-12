
list_seasons = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
dict_seasons = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето',
                9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}

while True:

    month = input('Введите номер месяца от 1 до 12 (пусто - выход): ')
    if month == '':
        break

    try:
        month_num = int(month)
        if month_num < 1 or month_num > 12:
            raise ValueError
        print(f'По списку это "{list_seasons[month_num-1]}", а по словарю "{dict_seasons.get(month_num)}"')
    except ValueError:
        print('Было ясно сказано - номер месяца от 1 до 12')
