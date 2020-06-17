def power(base: float, degree: int):
    return base ** degree


def power2(base: float, degree: int):
    prod = base
    while degree < -1:
        prod *= base
        degree += 1
    return 1 / prod

while True:
    base = input('Typed base (empty - exit): ')
    if base == '':
        break

    degree = input('Typed degree (empty - exit): ')
    if degree == '':
        break

    try:
        base = float(base)
        degree = int(degree)
        if base < 0:
            raise ValueError('Value base must be positive')
        if degree > 0:
            raise ValueError('Value degree must be negative')
        print('Result : ', power(base, degree))
        print('Result2: ', power2(base, degree))
    except ValueError as e:
        print('Invalid value: ', e)
