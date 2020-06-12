text = input('Введите текст: ')

i = 1
for token in text.split():
    print(f'{i}: {token[0:10]}')
    i += 1