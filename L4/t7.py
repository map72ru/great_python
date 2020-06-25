from math import factorial

def fact(max_fact: int):
    for n in list(range(1, max_fact)):
        yield factorial(n)


n = input('Enter n for factorial (empty - exit): ')

if n == '':
    exit(0)

try:
    n = int(n)
    for f in fact(n + 1):
        print(f)

except ValueError:
    print('invalid integer value: ', n)
