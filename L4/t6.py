'''Не понятно, зачем функция count. По условию: элементы некоторого списка, определенного заранее'''
from itertools import count, cycle

def gen_int(start: int, stop: int):
    n = start
    while n < stop:
        n += 1
        yield n

for a in gen_int(3, 10):
    print(a)


orig_list = ['mike', 'jonh', 'andrew', 'philip', 'bob', 'lui']
'''Количество повторений исходного массива'''
n = 5
for elm in cycle(orig_list):
    print(elm)
    if orig_list.index(elm) == len(orig_list)-1:
        n -= 1
        if n == 0:
            break


