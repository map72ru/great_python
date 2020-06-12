inp_values = []
inp = 'ignored'

while inp != '':
    inp = input('Введите значение (пустое значение - выход):')
    if inp != '':
        inp_values.append(inp)

if len(inp_values) == 0:
    print('Пустой массив. Уходим')
    exit(0)

print(f'Исходный архив        : {inp_values}')

i = 0
inp_len = len(inp_values)

while i < inp_len:
    if i+1 < inp_len:
        temp = inp_values[i]
        inp_values[i] = inp_values[i+1]
        inp_values[i+1] = temp
    i += 2

print(f'Модифицированный архив: {inp_values}')

