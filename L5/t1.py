file = None
try:
    file = open('task_1.txt', 'a')
    while True:
        usr_input = input('Введите либое значение (пусто: выход): ')
        if usr_input == '':
            break
        file.write(usr_input + '\nv')
finally:
    if file is not None:
        file.close()