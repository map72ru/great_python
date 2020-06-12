required_types = [int, int, float, str,  str, float]
inp_values = []

for required_type in required_types:
    inp = input(f'Введите значение типа {required_type.__name__} (пустое значение - выход):')
    if inp == '':
        exit(0)
    try:
        inp_values.append(required_type(inp))
    except ValueError as e:
        print(f'Введено неверное значение. Ошибка: {e}')

print(f'Введены правильные данные: {inp_values}')
