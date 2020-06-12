ratings = [10, 5, 2]
print(f'Начальный рейтинг: {ratings}')

while True:
    rating = input('Введите рейтинг как натуральное число (пусто - выход): ')
    if rating == '':
        break

    try:
        rating = int(rating)
        if rating < 1:
            raise ValueError

        found = False
        n = 0
        for item in ratings:
            if item < rating:
                ratings.insert(n, rating)
                break
            n += 1

        if n == len(ratings):
            ratings.append(rating)

        print(f'Новый рейтинг: {ratings}')
    except ValueError:
        print('Введено не верное число')
