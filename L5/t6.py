from math import fsum

def get_number(val: str):
    if val != '-':
        return int(val[0:val.index('(')])
    return 0


with open('task_6.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    themes = {}
    for line in lines:
        theme, other = line.split(':')
        alloc = other.split()
        themes.update({theme: fsum(map(get_number, other.split()))})

    print(themes)
