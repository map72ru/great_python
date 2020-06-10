distance = float(input('Typed distance in first day (km): '))
max_distance = float(input('Typed max distance (km): '))

n = 1
while distance <= max_distance:
    n += 1
    distance *= 1.1

print('Days: ', n)
