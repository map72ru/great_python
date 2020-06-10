while True:
    secondes = int(input('Get time in seconds (0 - exit): '))
    if secondes == 0:
        break
    print(f'{secondes // 3600:02d}:{secondes // 60 - 60 * (secondes // 3600):02d}:{secondes % 60:02d}')
