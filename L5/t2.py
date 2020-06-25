file = None
try:
    file = open('task_2.txt', 'r')
    lines = file.readlines()
    print(f'Строк: {len(lines)}')
    for i, line in enumerate(lines):
        print(f'В {i} строке {len(line.split())} слов')
finally:
    if file is not None:
        file.close()