from math import factorial

def fact(fact: int):
    n = 1
    while True:
        yield n
        if fact / factorial(n) == 1:
            break
        n += 1


n = input('Enter n for factorial (empty - exit): ')

if n == '':
    exit(0)

try:
    n = int(n)
    for f in fact(factorial(n)):
        print(f)

except ValueError:
    print('invalid integer value: ', n)
