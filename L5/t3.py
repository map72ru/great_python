file = None
try:
    file = open('task_3.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    sum = 0
    for line in lines:
        family, salary = line.split()
        salary = float(salary)
        if salary < 20000:
            print(f'{family}: {salary}')
        sum += salary
    if len(lines) > 0:
        print(f'Средний доход: {sum/len(lines)}')
    else:
        print('Данные отсутствуют')
finally:
    if file is not None:
        file.close()