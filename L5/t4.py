with open('task_4.txt', 'r', encoding='utf-8') as file:
    with open('task_4.out', 'w', encoding='utf-8') as out_file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('One'):
                out_file.write(line.replace('One', 'Один'))
            elif line.startswith('Two'):
                out_file.write(line.replace('Two', 'Два'))
            elif line.startswith('Three'):
                out_file.write(line.replace('Three', 'Три'))
            elif line.startswith('Four'):
                out_file.write(line.replace('Four', 'Четыре'))
            else:
                print('Не обрабатываемое значение числа: ', line)
