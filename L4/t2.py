import random

size = input('Enter list size (empty - exit)')

if size == '':
    exit(0)

try:
    '''Генерируем список'''
    size = int(size)
    numbers = list((random.randint(0, 1000) for n in range(0, size)))
    '''Вычисляем число большее предыдущего'''
    max_numbers = list((item for item in numbers[1:] if item > numbers[numbers.index(item)-1]))

    print('Source list: ', numbers)
    print('Rsult: ', max_numbers)
except ValueError:
    print('invalid list size: ', size)
