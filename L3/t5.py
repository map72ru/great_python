def summator(summa: float, value_list: list):
    for value in value_list:
        if str(value).upper() == 'Q':
            break

        if not str(value).replace('.', '').isdigit():
            raise ValueError(f'Invalid value in list (not a number): {value}')

        summa += float(value)

    return summa


sum = 0
while True:
    try:
        values = input('Typed list of number (q - terminator. empty - exit, enter - mske sum, space - devider): ')
        result = summator(sum, values.split())
        print(f'Result: {result}')
        sum = result
    except Exception as x:
        print(f'Input error: {x}')
