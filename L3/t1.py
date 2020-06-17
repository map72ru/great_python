def divider(dividend, devdr):
    if devdr == 0:
        raise Exception('Devider is null')
    return dividend / devdr


while True:
    dividen = input('Type deviden (empty - exit): ')
    if dividen == '':
        break

    divdr = input('Type devider (empty - exit): ')
    if divdr == '':
        break

    try:
        print('Result: ', divider(float(dividen), float(divdr)))
    except ValueError as e:
        print('Invalid value: ', e)
    except Exception as x:
        print('Error: ', x)
